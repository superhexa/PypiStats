from google.cloud import bigquery
from google.oauth2 import service_account

class PypiStats:
    def __init__(self, project_id, credentials_path):
        self.credentials = service_account.Credentials.from_service_account_file(credentials_path)
        self.client = bigquery.Client(project=project_id, credentials=self.credentials)

    def get_total_downloads(self, project_name):
        query = f"""
            SELECT IFNULL(SUM(CASE WHEN file.project = '{project_name}' THEN 1 ELSE 0 END), 0) AS downloads
            FROM `bigquery-public-data.pypi.file_downloads`
        """
        result = self.client.query(query).result().to_dataframe()
        return result['downloads'].iloc[0] if result['downloads'].iloc[0] > 0 else False
