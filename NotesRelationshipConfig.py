class NotesRelationshipConfig(object):
    evaluate_one_step = True
    evaluate_two_steps = True
    evaluate_three_steps = True
    evaluate_same_distance = True

    def __init__(self, evaluate_one_step, evaluate_two_steps, evaluate_three_steps, evaluate_same_distance):
        self.evaluate_one_step = evaluate_one_step
        self.evaluate_two_steps = evaluate_two_steps
        self.evaluate_three_steps = evaluate_three_steps
        self.evaluate_same_distance = evaluate_same_distance
