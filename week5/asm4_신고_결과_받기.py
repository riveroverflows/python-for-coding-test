def solution(id_list, report, k):
    reporters_dict = {}
    respondents_dict = {}
    for reporter_respondent in report:
        reporter, respondent = reporter_respondent.split()
        respondents_by_reporter = reporters_dict.get(reporter, [])
        respondents_by_reporter.append(respondent)
        reporters_dict[reporter] = respondents_by_reporter

        reporters_by_respondent = respondents_dict.get(respondent, set())
        reporters_by_respondent.add(reporter)
        respondents_dict[respondent] = set(reporters_by_respondent)

    suspendeds = set([respondent for respondent, reporters in respondents_dict.items() if len(reporters) >= k])
    answer = []
    for id_ in id_list:
        respondents_by_id = reporters_dict.get(id_, [])
        answer.append(len(set(respondents_by_id).intersection(suspendeds)))
    return answer
