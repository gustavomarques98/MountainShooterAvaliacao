#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, WIN_HEIGHT
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        self.direction = "up"

    def move(self):

        if self.name == "Enemy3":
            # Movimentação horizontal
            self.rect.centerx -= ENTITY_SPEED[self.name]

            # Movimentação vertical controlada pela direção
            if self.direction == "up":
                # Sobe com velocidade normal
                self.rect.centery -= ENTITY_SPEED[self.name]
                if self.rect.centery <= 0:  # Se atingir o topo da tela
                    self.direction = "down"  # Altera a direção para baixo
            elif self.direction == "down":
                # Desce com o dobro da velocidade
                self.rect.centery += ENTITY_SPEED[self.name] * 2
                if self.rect.centery >= WIN_HEIGHT:  # Se atingir a parte inferior da tela
                    self.direction = "up"
        else:
            self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
