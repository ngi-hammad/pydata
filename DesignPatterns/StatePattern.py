"""
State is a behavioral design pattern that allows an object
to change the behavior when its internal state changes.

Usage examples: The State pattern is commonly used in Python
to convert massive switch-base state machines into the objects.

Identification: State pattern can be recognized by methods that
change their behavior depending on the objects’ state, controlled externally.
"""

from abc import ABC, abstractmethod


class Context:
    """
        The Context defines the interface of interest to clients. It also maintains
        a reference to an instance of a State subclass, which represents the current
        state of the Context.
    """

    _state = None

    def __init__(self, state):
        self.transition_to(state)

    def transition_to(self, state):
        print(f"Context: Transition to {type(state).__name__}")
        self._state = state
        self._state.context = self

    def request1(self):
        self._state.handle1()

    def request2(self):
        self._state.handle2()


class State(ABC):
    """
        The base State class declares methods that all Concrete State should
        implement and also provides a backreference to the Context object,
        associated with the State. This backreference can be used by States to
        transition the Context to another State.
    """

    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, context):
        self._context = context

    @abstractmethod
    def handle1(self):
        pass

    @abstractmethod
    def handle2(self):
        pass


class ConcreteStateA(State):
    def handle1(self):
        print("ConcreteStateA handles request1.")
        print("ConcreteStateA wants to change the state of the context.")
        self.context.transition_to(ConcreteStateB())

    def handle2(self):
        print("ConcreteStateA handles request2.")


class ConcreteStateB(State):
    def handle1(self):
        print("ConcreteStateB handles request1.")

    def handle2(self):
        print("ConcreteStateB handles request2.")
        print("ConcreteStateB wants to change the state of the context.")
        self.context.transition_to(ConcreteStateA())


if __name__ == "__main__":
    # The client code.

    context = Context(ConcreteStateA())
    context.request1()
    context.request2()