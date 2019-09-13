from music21 import interval
from music21 import scale
from music21.note import Note
from MusicNote import MusicNote
import random


class MusicPeace(object):
    all_notes = []
    temp_notes = []
    bars_number = 0
    note_ids = []

    def __init__(self, bars_number):
        self.bars_number = bars_number
        self.get_all_notes(0.0)

    def get_all_notes(self, note_fitness_score):
        self.get_temp_notes()
        self.create_notes(note_fitness_score)

    def get_temp_notes(self):
        count = 0
        bars_count = 0
        while bars_count < self.bars_number * 4:
            tone = self.generate_scale_tone(self.temp_notes, count)
            self.temp_notes.append(tone)
            bars_count = self.calculate_if_bars_are_done()
            count = count + 1

    def calculate_if_bars_are_done(self):
        count = 0
        for note in self.temp_notes:
            count = count + note.duration.quarterLength
        return count

    @staticmethod
    def generate_scale_tone(notes: [], count):
        items = ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C#', 'D#', 'F#', 'G#', 'A#']

        rand_item = items[random.randrange(len(items))]

        scales = scale.MajorScale(rand_item)

        all_pitches = list(set([pitch for pitch in scales.getPitches()]))
        all_note_names = [i.name for i in all_pitches]

        note_name = random.choice(all_note_names)

        final_note = Note(note_name)

        duration_list = [1, 1 / 2]

        if not notes:
            final_note.duration.quarterLength = random.choice(duration_list)
            return final_note

        try:
            if notes[count - 1].duration.quarterLength == 1 / 2 and notes[count - 2].duration.quarterLength != 1 / 2:
                final_note.duration.quarterLength = 1 / 2
                return final_note
        except:
            if count == 0:
                final_note.duration.quarterLength = 1 / 2
                return final_note
            else:
                pass
        else:
            final_note.duration.quarterLength = random.choice(duration_list)
            return final_note

    def create_notes(self, note_fitness_score):
        for index in range(0, len(self.temp_notes)):
            note = self.temp_notes[index]

            if index + 1 >= len(self.temp_notes):
                note_interval = interval.Interval(note, second_note)
                self.all_notes.append(MusicNote(note, note_fitness_score, note_interval, index, is_last=True))
                continue

            second_note = self.temp_notes[index + 1]
            note_interval = interval.Interval(note, second_note)

            if index == 0:
                self.all_notes.append(MusicNote(note, note_fitness_score, note_interval, index))
                continue

            self.all_notes.append(MusicNote(note, note_fitness_score, note_interval, index))
