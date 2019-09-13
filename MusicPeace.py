from music21 import interval
from MusicNote import MusicNote
from GeneticAlgortihm import generate_scale_tone
import random


class MusicPeace(object):
    all_notes = []
    temp_notes = []
    bars_number = 0
    note_ids = []

    def __init__(self, bars_number) -> object:
        self.bars_number = bars_number
        self.get_all_notes(0.0)

    def get_all_notes(self, note_fitness_score):
        self.get_temp_notes()
        self.create_notes(note_fitness_score)

    def get_temp_notes(self):
        count = 0
        bars_count = 0
        while bars_count < self.bars_number * 4:
            tone = generate_scale_tone(self.temp_notes, count)
            self.temp_notes.append(tone)
            bars_count = self.calculate_if_bars_are_done()
            count = count + 1

    def calculate_if_bars_are_done(self):
        count = 0
        for note in self.temp_notes:
            count = count + note.duration.quarterLength
        return count

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
