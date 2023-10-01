from repository.repository import find_all_by_city, find_by_uni_name, find_all_by_city_and_subject
from context.Context import Context
from service.executors.Executor import Executor


class FindStudiesExecutor(Executor):

    def execute(self, context: Context):
        if ['CITY'] == context.labels:
            tmp = context.doc.ents[0].text
            tmp_df = find_all_by_city(tmp)

            # TODO workaround for not big dataset
            if tmp_df.empty:
                context.response = find_all_by_city('Kraków')
            else:
                context.response = tmp_df

        elif ['UNIVERSITY'] == context.labels:
            tmp = context.doc.ents[0].text
            tmp_df = find_by_uni_name(tmp)

            # TODO workaround for not big dataset
            if tmp_df.empty:
                context.response = find_by_uni_name('Politechnika Krakowska')
            else:
                context.response = tmp_df

        elif ['CITY', 'SUBJECT'] == context.labels:
            tmp = context.doc.ents[0].text
            tmp_df = find_by_uni_name(tmp)

            if tmp_df.empty:
                context.response = find_all_by_city_and_subject('Politechnika Krakowska')
            else:
                context.response = tmp_df