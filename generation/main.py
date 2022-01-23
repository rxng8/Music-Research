"""
  Author: Alex Nguyen
  File name: main.py
  Description: 
"""
# %%

import collections
import os

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

import mido
from amg.roll import MidiFile


DATASET_FOLDER = "./dataset/JSB Chorales"
TRAIN_FOLDER = os.path.join(DATASET_FOLDER, "train")
TEST_FOLDER = os.path.join(DATASET_FOLDER, "test")
VAL_FOLDER = os.path.join(DATASET_FOLDER, "val")

SAMPLE_RATE = 44100

# sample_midi = mido.MidiFile(os.path.join(TEST_FOLDER, "9.mid"), clip=True)
sample_midi = MidiFile("./dataset/demo/All Night Long.mid", clip=True)

def summarize_midi(midi: MidiFile):
  """ Summarize a midi file

  Args:
    midi_file (mido.MidiFile): [description]
  """
  print(f"Midi type: {midi.type}, ticks_per_beat: {midi.ticks_per_beat}")
  print(f"Number of tracks: {len(midi.tracks)}", end="\n")
  for i, track in enumerate(midi.tracks):
    print(f"Track {i + 1}:")
    print(f"Track messages length: {len(track)}")
    count = collections.Counter()
    meta = collections.defaultdict(list)
    for message in track:
      count["program_change"] += (1 if message.type=="program_change" else 0)
      count["control_change"] += (1 if message.type=="control_change" else 0)
      count["note_on"] += (1 if message.type=="note_on" else 0)
      count["note_off"] += (1 if message.type=="note_off" else 0)
      if type(message) is mido.MetaMessage:
        if message.type == "track_name":
          meta["track_name"].append(message.name)
        elif message.type == "copyright":
          meta["copyright"].append(message.text)
        elif message.type == "midi_port":
          meta["midi_port"].append(message.port)
        elif message.type == "time_signature":
          meta["time_signature"].append((message.numerator, message.denominator))
        elif message.type == "key_signature":
          meta["key_signature"].append(message.key)
        elif message.type == "set_tempo":
          meta["set_tempo"].append(message.tempo)
    print(meta)
    print(count)

summarize_midi(sample_midi)

# %%
sample_midi


# %%


sample_midi.draw_roll()

# %%


sample_midi.get_total_ticks()
