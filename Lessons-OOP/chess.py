class Board:
    def __init__(self):
        self.field = []

        colour = 'black'
        self.field.append({'piece': Rook(colour), 'position': (0, 7)})
        self.field.append({'piece': Knight(colour), 'position': (1, 7)})
        self.field.append({'piece': Bishop(colour), 'position': (2, 7)})
        self.field.append({'piece': Queen(colour), 'position': (3, 7)})
        self.field.append({'piece': King(colour), 'position': (4, 7)})
        self.field.append({'piece': Bishop(colour), 'position': (5, 7)})
        self.field.append({'piece': Knight(colour), 'position': (6, 7)})
        self.field.append({'piece': Rook(colour), 'position': (7, 7)})
        self.field.append({'piece': Pawn(colour), 'position': (0, 6)})
        self.field.append({'piece': Pawn(colour), 'position': (1, 6)})
        self.field.append({'piece': Pawn(colour), 'position': (2, 6)})
        self.field.append({'piece': Pawn(colour), 'position': (3, 6)})
        self.field.append({'piece': Pawn(colour), 'position': (4, 6)})
        self.field.append({'piece': Pawn(colour), 'position': (5, 6)})
        self.field.append({'piece': Pawn(colour), 'position': (6, 6)})
        self.field.append({'piece': Pawn(colour), 'position': (7, 6)})

        colour = 'white'
        self.field.append({'piece': Rook(colour), 'position': (0, 0)})
        self.field.append({'piece': Knight(colour), 'position': (1, 0)})
        self.field.append({'piece': Bishop(colour), 'position': (2, 0)})
        self.field.append({'piece': Queen(colour), 'position': (3, 0)})
        self.field.append({'piece': King(colour), 'position': (4, 0)})
        self.field.append({'piece': Bishop(colour), 'position': (5, 0)})
        self.field.append({'piece': Knight(colour), 'position': (6, 0)})
        self.field.append({'piece': Rook(colour), 'position': (7, 0)})
        self.field.append({'piece': Pawn(colour), 'position': (0, 1)})
        self.field.append({'piece': Pawn(colour), 'position': (1, 1)})
        self.field.append({'piece': Pawn(colour), 'position': (2, 1)})
        self.field.append({'piece': Pawn(colour), 'position': (3, 1)})
        self.field.append({'piece': Pawn(colour), 'position': (4, 1)})
        self.field.append({'piece': Pawn(colour), 'position': (5, 1)})
        self.field.append({'piece': Pawn(colour), 'position': (6, 1)})
        self.field.append({'piece': Pawn(colour), 'position': (7, 1)})

class BasePiece:
    def __init__(self,colour):
        if type(colour) != str:
            raise TypeError('colour argument must be str')
        elif colour.lower() not in {'white','black'}:
            raise ValueError('colour must be {white,black}')
        else:
            self.colour = colour

    def __repr__(self):
        return f'BasePiece({repr(self.colour)})'
    
    def __str__(self):
        try:
            # define __str__() to return a simple description
            # e.g. 'white king', 'black queen'
            ### BEGIN SOLUTION
            return f'{self.colour} {self.name}'
            ### END SOLUTION
        except NameError:
            return f'{self.colour} piece'
    
class King(BasePiece):
    name = 'king'
    def __repr__(self):
        return f'King({repr(self.colour)})'

class Queen(BasePiece):
    name = 'queen'
    def __repr__(self):
        return f'Queen({repr(self.colour)})'

class Bishop(BasePiece):
    name = 'bishop'
    def __repr__(self):
        return f'Bishop({repr(self.colour)})'

class Knight(BasePiece):
    name = 'knight'
    def __repr__(self):
        return f'Knight({repr(self.colour)})'

class Rook(BasePiece):
    name = 'rook'
    def __repr__(self):
        return f'Rook({repr(self.colour)})'

class Pawn(BasePiece):
    name = 'pawn'
    def __repr__(self):
        return f'Pawn({repr(self.colour)})'