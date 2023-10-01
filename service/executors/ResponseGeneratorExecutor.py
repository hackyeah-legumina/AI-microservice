from context.Context import Context
from service.executors.Executor import Executor


class ResponseGeneratorExecutor(Executor):

    def execute(self, context: Context):
        try:
            context.response = self.create_response(context.response)
        except:
            context.response = self.create_response(context.response[0])

    def create_response(self, response):
        return {
            "Universities": {
                "id": response['Id'].values[0],
                "institutionName": response['Nazwa instytucji'].values[0],
                "creationDate": response['Data utworzenia / data wpisu do ewiencji uczelni niepublicznych'].values[0],
                "institutionType": response['Rodzaj instytucji'].values[0],
                "universityType": "",
                "regon": response['Instytucje dziedziczące - REGON'].values[0],
                "nip": response['Instytucje dziedziczące - NIP'].values[0],
                "krs": "",
                "website": response['Strona www'].values[0],
                "streetAddress": response['Adres - ulica'].values[0],
                "streetNumber": response['Adres - numer'].values[0],
                "postalCode": response['Adres - kod pocztowy'].values[0],
                "city": response['Adres - miasto'].values[0]
            }
        }
