from music21.note import Note


class MusicNote(object):
    location = 0
    fitness_score = 0.0
    melody_direction_fitness = 0
    is_first_note_of_melody = False
    is_last_note_of_melody = False
    note_interval = None

    def __init__(self, music_note: Note, fitness_score: 0.0, note_interval, location, is_last=False):
        self.note_interval = note_interval
        self.music_note = music_note
        self.fitness_score = fitness_score
        self.location = location
        if location == 0:
            self.is_first_note_of_melody = True
        self.is_last_note_of_melody = is_last

    def __repr__(self):
        return repr(self.fitness_score)
