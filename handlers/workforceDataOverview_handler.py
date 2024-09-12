from handlers.base_handler import BaseHandler

class WorkforceDataOverviewHandler(BaseHandler):
    def __init__(self, data, logger=None):
        super().__init__(data, logger)
    def manipulate_data(self):
        for row in self.data:
            
            # workforceId is just string
            row['workforceId'] = str(int(row['workforceId']))
            
            if row['skills'] is not None:
                role_id_list = row['skills'].split(',')
                # Filter out any empty strings resulting from extra commas
                role_id_list = [uuid for uuid in role_id_list if uuid]
                # Create a list of dictionaries with each UUID
                skills_list = [{'roleId': uuid} for uuid in role_id_list]
                row['skills'] = skills_list
            else:
                row['skills'] = []
            # print(row)
        return self.data
