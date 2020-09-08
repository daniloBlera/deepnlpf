#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Implementation of a simple processing pipeline for testing

Below are some usage examples for the stanza, spacy, scispacy and stanza-bio:
    echo 'Barack Obama was born in Hawaii.' | python3 pipeline.py pipeline-stanza.json
    echo 'Apple is looking at buying U.K. startup for $1 billion' | python3 pipeline.py pipeline-spacy.json
    echo 'Myeloid derived suppressor cells (MDSC) are immature myeloid cells with immunosuppressive activity.' | python3 pipeline.py pipeline-scispacy.json
    echo 'A single-cell transcriptomic atlas characterizes ageing tissues in the mouse.' | python3 pipeline.py pipeline-stanza-bio.json
"""
import argparse
import os
import sys

from deepnlpf.pipeline import Pipeline


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='A generic testing pipeline using inputs from stdin')
    parser.add_argument('PIPELINE_PATH', type=str,
            help='The path to a pipeline')

    args = parser.parse_args()
    lines = [l.rstrip() for l in sys.stdin]
    rawtext = os.linesep.join(lines)

    if not os.path.exists(args.PIPELINE_PATH):
        print(f'ERROR: File {args.PIPELINE_PATH} not found!', file=sys.stderr)
        exit(1)

    nlp = Pipeline(_input=rawtext, pipeline=args.PIPELINE_PATH, _output='file')
    nlp.annotate()
