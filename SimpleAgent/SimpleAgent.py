"""
SimpleAgent - A minimalist AI agent framework

This script implements a simple AI agent that can perform basic operations
through function calling. It uses the OpenAI API to generate responses and
execute functions based on user instructions.
"""

import os
import sys
import json
import time
import argparse
from typing import List, Dict, Any, Optional, Callable

# Import commands package
import commands
from commands import REGISTERED_COMMANDS, COMMAND_SCHEMAS

# Import core modules
from core.agent import SimpleAgent
from core.config import OPENAI_API_KEY, MAX_STEPS

# Initialize commands
commands.init()

# Check for API key
if not OPENAI_API_KEY:
    print("Error: OPENAI_API_KEY environment variable not set.")
    print("Please set it in a .env file or in your environment variables.")
    sys.exit(1)


def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='SimpleAgent - An AI agent that can perform tasks')
    # Add flags first to prevent instruction from being consumed as a flag value
    parser.add_argument('-a', '--auto', type=int, nargs='?', const=10, default=0,
                      help='Auto-continue for N steps (default: 10 if no number provided)')
    parser.add_argument('-m', '--max-steps', type=int, default=10,
                      help='Maximum number of steps to run (default: 10)')
    parser.add_argument('instruction', nargs='+', help='The instruction for the AI agent')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Join the instruction parts back together
    instruction = ' '.join(args.instruction)
    
    # Ensure max_steps is at least as large as auto_continue
    max_steps = max(args.max_steps, args.auto) if args.auto > 0 else args.max_steps
    
    # Initialize and run the agent
    agent = SimpleAgent()
    agent.run(instruction, max_steps=max_steps, auto_continue=args.auto)


if __name__ == "__main__":
    main() 