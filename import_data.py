import sys
import os
import django

# Set the base directory (where manage.py is)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Add the base directory and the inner project directory to sys.path
sys.path.append(BASE_DIR)
sys.path.append(os.path.join(BASE_DIR, "voter_management"))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

import pandas as pd
from django.db import transaction
from voters.models import Voter, VoterField


def detect_field_type(series):
    """
    Detect the type of data in a pandas series
    """
    if series.dtype == 'bool':
        return 'boolean'
    elif series.dtype == 'object':
        return 'text'
    elif 'int' in str(series.dtype):
        return 'number'
    elif 'float' in str(series.dtype):
        return 'decimal'
    elif 'datetime' in str(series.dtype):
        return 'datetime'
    return 'text'


@transaction.atomic
def import_excel_data(file_path):
    """
    Import data from Excel file and create voter records
    """
    try:
        # Read Excel file
        df = pd.read_excel(file_path)

        # Create fields first
        fields_to_create = []
        for column in df.columns:
            field_type = detect_field_type(df[column])
            fields_to_create.append(
                VoterField(
                    name=column,
                    field_type=field_type,
                    is_required=True  # You can modify this based on your requirements
                )
            )

        # Bulk create fields, ignore if they already exist
        VoterField.objects.bulk_create(
            fields_to_create,
            ignore_conflicts=True
        )

        # Prepare voter data
        voters_data = []
        for _, row in df.iterrows():
            voter_data = row.to_dict()
            # Handle non-serializable values
            for key, value in voter_data.items():
                if pd.isna(value):
                    voter_data[key] = None
                elif isinstance(value, pd.Timestamp):
                    voter_data[key] = value.isoformat()
                else:
                    voter_data[key] = str(value)

            voters_data.append(Voter(data=voter_data))

        # Bulk create voters
        Voter.objects.bulk_create(voters_data)

        return len(voters_data)

    except Exception as e:
        raise Exception(f"Error importing data: {str(e)}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: /Users/adititomar/PycharmProjects/voter_management/data/28-TIRUVURU.xlsx")
        sys.exit(1)

    file_path = sys.argv[1]
    imported_count = import_excel_data(file_path)
    print(f"Successfully imported {imported_count} voters.")
