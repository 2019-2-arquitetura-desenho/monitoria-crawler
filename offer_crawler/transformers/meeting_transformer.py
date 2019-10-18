from offer_crawler.transformers.transformer import JsonTransformer
import json
import collections

class MeetingTransformer(JsonTransformer):
    pk = 1
    meetings = []

    def __init__(self, meeting):
        self.map_meeting = collections.defaultdict(dict)
        self.meeting = meeting

    def define_model(self) -> None:
        self.map_meeting["model"] = "offers.meeting"

    def define_pk(self) -> None:
        self.map_meeting["pk"] = MeetingTransformer.pk
        MeetingTransformer.pk += 1

    def define_fields(self, meeting) -> None:
        self.map_meeting["fields"]["day"] = self.meeting.getName()
        self.map_meeting["fields"]["init_hout"] = self.meeting.getName()
        self.map_meeting["fields"]["final_hout"] = self.meeting.getName()
        self.map_meeting["fields"]["room"] = self.meeting.getName()
        self.map_meeting["fields"]["discipline_class"] = self.meeting.getName()
        print(self.map_meeting)
        MeetingTransformer.meetings.append(self.map_meeting)
    
    def write_json(self):
        with open('offers/fixtures/meeting.json', "w") as f:
            json.dump(MeetingTransformer.meetings, f, indent=4)
            