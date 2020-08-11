import abc
import math


class EloManagerInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'get_new_elos') 
                and callable(subclass.get_new_elos)
                and hasattr(subclass, 'get_match_probabilities') 
                and callable(subclass.get_match_probabilities))

    @abc.abstractclassmethod
    def get_new_elos(self, old_elos: [int], result: int):
        """
        Calculate the new elos based on the old elos and result of a game.
        """
        raise NotImplementedError

    @abc.abstractclassmethod
    def get_match_probabilities(self, elos: [int]):
        """ Get the probability for each elo to win. """
        raise NotImplementedError


class WinRateEloManager(EloManagerInterface):
    def get_new_elos(self, old_elos: [int], result: int):
        k = 30
        probabilites = self.get_match_probabilities(old_elos)
        if result == -1:
            scores = [1.0 / len(old_elos) for _ in range(len(old_elos))]
        else:
            scores = [
                1 if index == result else 0 for index in range(
                    len(old_elos))]

        return [old_elos[i] + k * (scores[i] - probabilites[i])
                for i in range(len(old_elos))]

    def get_match_probabilities(self, elos: [int]):
        total_elo = sum(elos)
        return [1.0 / (1.0 + pow(10, (2 * elo - total_elo / 400)))
                for elo in elos]
