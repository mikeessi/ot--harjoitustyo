import pygame

class Hitboxes:

    def __init__(self, positions, card_size):

        self.discardpile_rect = pygame.Rect(positions["discard"], card_size)
        self.drawpile_rect = pygame.Rect(positions["draw"], card_size)

        self.endpile_rects = []
        for suit in range(4):
            self.endpile_rects.append(pygame.Rect(positions[f"empty_{suit}"], card_size))

        self.tableau_rects = []
        self.tableau_union_rects = []

        for tabl_id in range(7):
            pos_base = positions[f"tableau_{tabl_id}"]
            single_pile_rects = []
            pos_adjust = 0
            for i in range(20):
                pos = (pos_base[0],pos_base[1]+pos_adjust)
                single_pile_rects.append(pygame.Rect(pos,card_size))
                pos_adjust += 20
            self.tableau_rects.append(single_pile_rects)

        for sequence in self.tableau_rects:
            first_rect = sequence[0]
            union_rect = first_rect.unionall(sequence[1:])
            self.tableau_union_rects.append(union_rect)

        self.rectangles = {
            "discard": [self.discardpile_rect],
            "draw": [self.drawpile_rect],
            "tableau": self.tableau_union_rects,
            "endpile": self.endpile_rects
        }

    def check_rects(self, mouse_pos):
        if self.check_drawpile(mouse_pos) is not None:
            return self.check_drawpile(mouse_pos)
        elif self.check_discardpile(mouse_pos) is not None:
            return self.check_discardpile(mouse_pos)
        elif self.check_endpiles(mouse_pos) is not None:
            return self.check_endpiles(mouse_pos)
        elif self.check_tableaus(mouse_pos) is not None:
            return self.check_tableaus(mouse_pos)
        else:
            return None, None, None

    def check_lists(self, mouse_pos, rect_list, reverse):
        if reverse:
            rects = reversed(list(enumerate(rect_list)))
        else:
            rects = enumerate(rect_list)

        for rect_index, rect in rects:
            if rect.collidepoint(mouse_pos):
                return rect_index
        return None

    def check_endpiles(self, mouse_pos):
        endpile_index = self.check_lists(mouse_pos, self.endpile_rects, False)
        if endpile_index is not None:
            return "endpile", endpile_index, None

        return None

    def check_drawpile(self, mouse_pos):
        drawpile = self.check_lists(mouse_pos, [self.drawpile_rect], False)
        if drawpile is not None:
            return "drawpile", drawpile, None

        return None

    def check_discardpile(self, mouse_pos):
        discardpile = self.check_lists(mouse_pos, [self.discardpile_rect], False)
        if discardpile is not None:
            return "discardpile", discardpile, None

        return None

    def check_tableaus(self, mouse_pos):
        tableau_index = self.check_lists(mouse_pos, self.tableau_union_rects, False)
        if tableau_index is not None:
            tableau = self.tableau_rects[tableau_index]
            tableau_rank = self.check_lists(mouse_pos, tableau, True)
            return "tableau", tableau_index, tableau_rank

        return None
