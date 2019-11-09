from crawler.transformers.transformer import JsonTransformer
import collections

class MeetingTransformer(JsonTransformer):
    pk = 1
    meetings = []

    def __init__(self, fk, meeting):
        self.map_meeting = collections.defaultdict(dict)
        self.fk = fk
        self.meeting = meeting

    def define_model(self) -> None:
        self.map_meeting["model"] = "offers.meeting"

    def define_pk(self) -> None:
        self.map_meeting["pk"] = MeetingTransformer.pk
        MeetingTransformer.pk += 1

    def define_fields(self, meeting) -> None:
        self.map_meeting["fields"]["day"] = self.meeting["day"]
        self.map_meeting["fields"]["init_hour"] = self.meeting["init_hour"]
        self.map_meeting["fields"]["final_hour"] = self.meeting["final_hour"]
        self.map_meeting["fields"]["room"] = self.meeting["room"]
        self.map_meeting["fields"]["discipline_class"] = self.fk
        MeetingTransformer.meetings.append(self.map_meeting)
