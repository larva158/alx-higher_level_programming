#!/usr/bin/node
import { argv } from 'node:process'
if ((argv === 1)) { console.log('No argument') };
if ((argv === 2)) { console.log('Argument found') };
if ((argv > 2)) { console.log('Arguments found') };
