from NotesRelationshipConfig import NotesRelationshipConfig


class AlgorithmConfig(object):
    notes_relationship_config = NotesRelationshipConfig(True, True, True, True)
    evaluate_degree = True
    evaluate_drastic_duration_change = True
    evaluate_note_melody_direction = True
    evaluate_first_or_last_note = True

    def __init__(self, evaluate_degree,
                 evaluate_drastic_duration_change,
                 evaluate_note_melody_direction,
                 evaluate_first_or_last_note,
                 notes_relationship_config: NotesRelationshipConfig):
        self.notes_relationship_config = notes_relationship_config
        self.evaluate_degree = evaluate_degree
        self.evaluate_drastic_duration_change = evaluate_drastic_duration_change
        self.evaluate_note_melody_direction = evaluate_note_melody_direction
        self.evaluate_first_or_last_note = evaluate_first_or_last_note
