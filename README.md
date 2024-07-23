# python-zero-to-mastery
## About
In this repo, I want to explore more about Python programming language. I will discuss 
hot-topic and useful libraries in this programming language, so you can have a deep understanding of 
whereabouts of this language. Python is really vast, so I will try to update it time to time. Thanks.

## Structure
### 1. Logging [`logging_zero_to_mastery.ipynb` & `logging_zero_to_mastery.py`]
- Basic Logging Example
- Larger Applications
- Logging to a File
- Logger Object
- Rotating Log Files
- Logging Exceptions
- Custom Level Logging

### 2. Testing [`testing_zero_to_mastery.ipynb`]
- Types of Software Testing
  - Manual Testing
  - Automated Testing
- Functional vs. Non-Functional
  - Definition
  - Functional Testing
    - Unit Testing
    - Integration Testing
    - System Testing
    - Acceptance Testing
  - Non-Functional Testing
    - Performance Testing
    - Load Testing
    - Security Testing
    - Usability Testing
  - Understanding the Difference [functional/non-functional vs. manual/automated]
- Code
  - Our Application
  - Write a Test Case
  - Analysis


### 3. Parallelism & Concurrency [`parallelism_zero_to_mastery.ipynb`]
- Understanding Concurrency & Parallelism
- Asyncio for Concurrency
  - Details
  - Asyncio Queue
  - asyncio.run()
  - asyncio.gather()
  - asyncio.create_task()
  - asyncio.sleep()
  - asyncio.wait()
  - asyncio.as_completed()
  - asyncio.shield()
- Threading for Concurrency
- Multiprocessing for Parallelism
- Threading vs Multiprocessing
  - Threading
  - Multiprocessing
  - Summary


### 4. Decorators & Metaclasses [`decorator__zero_to_mastery.ipynb`]
- Description
- Decorator
  - Function Decorators
  - Decorators with Arguments
  - Class Decorators
  - Advanced Function Decorators
    - Decorating Functions with Arguments
    - Chaining Decorators
    - Decorators with Optional Arguments
    - Retry Logic
  - Existing Decorators
    - @staticmethod & @classmethod
    - @property
    - @lru_cache (functools)
    - @dataclass (dataclasses)
    - @contextmanager (contextlib)
    - @cached_property (functools)
    - @dataclass with Field Customization
    - @retry (Third-Party Library - retrying)
- Metaclass
  - Creating a Metaclass
  - Enforcing Class Behavior
  - Singleton Metaclass


### 5. Data Serialization
- Description
- Python
  - JSON
  - Pickle
  - YAML
- Comparison

### 6. [MORE TO COME...]


## Remarks
### 1. Logging
You can find the log files in both `logs/app.log` or `./app.log` for outputs.
