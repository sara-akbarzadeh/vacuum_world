import random

class environment:
    def __init__(self):
        self.rooms = {
            (0, 0): 'dirty',
            (0, 1): 'dirty',
            (1, 0): 'dirty'
        }
        self.robot_position = (0, 0)  
    
    # def perceive(self):
    #     pass

    def move(self, action):
        if action == "up" and self.robot_position == (1, 0):
            self.robot_position = (1, 0)
        elif action == "up" and self.robot_position == (0, 0):
            self.robot_position = (1, 0)
        elif action == "up" and self.robot_position == (0, 1):
            self.robot_position = (0, 1)
        elif action == "left" and self.robot_position == (1, 0):
            self.robot_position = (1, 0)
        elif action == "left" and self.robot_position == (0, 0):
            self.robot_position = (0, 0)
        elif action == "left" and self.robot_position == (0, 1):
            self.robot_position = (0, 0)
        elif action == "right" and self.robot_position == (1, 0):
            self.robot_position = (1, 0)
        elif action == "right" and self.robot_position == (0, 0):
            self.robot_position = (0, 1)
        elif action == "right" and self.robot_position == (0, 1):
            self.robot_position = (0, 1)
        elif action == "down" and self.robot_position == (1, 0):
            self.robot_position = (0, 0)
        elif action == "down" and self.robot_position == (0, 0):
            self.robot_position = (0, 0)
        elif action == "down" and self.robot_position == (0, 1):
            self.robot_position = (0, 1)


    def vacuum(self):
        if self.rooms[self.robot_position] == 'dirty':
            self.rooms[self.robot_position] = 'clean'


class env_fullyObs_deterministic_static(environment):
    def perceive(self):
        return {
            'position': self.robot_position,
            'cleanliness': self.rooms.copy()
        }


class env_fullyObs_deterministic_dynamic(environment):
    def perceive(self):
        """Fully observable and deterministic with rooms potentially becoming dirty again."""
        return {
            'position': self.robot_position,
            'cleanliness': self.rooms.copy()
        }
    
    def move(self, action):
        super().move(action)
    
    def dynamic_dirtying(self):
        for room in self.rooms:
            if random.random() < 0.2:  
                self.rooms[room] = 'dirty'


class env_fullyObs_stochasticInMove_static(environment):
    def perceive(self):
        return {
            'position': self.robot_position,
            'cleanliness': self.rooms.copy()
        }
    
    def move(self, action):
        if random.random() > 0.2:  
            super().move(action)


class env_fullyObs_stochasticInMove_dynamic(environment):
    def perceive(self):
        return {
            'position': self.robot_position,
            'cleanliness': self.rooms.copy()
        }
    
    def move(self, action):
        if random.random() > 0.2:  
            super().move(action)
    
    def dynamic_dirtying(self):
        for room in self.rooms:
            if random.random() < 0.2:
                self.rooms[room] = 'dirty'


class env_fullyObs_stochasticInVac_static(environment):
    def perceive(self):
        return {
            'position': self.robot_position,
            'cleanliness': self.rooms.copy()
        }
    
    def vacuum(self):
        if random.random() > 0.2:  
            super().vacuum()


class env_fullyObs_stochasticInVac_dynamic(environment):
    def perceive(self):
        return {
            'position': self.robot_position,
            'cleanliness': self.rooms.copy()
        }
    
    def vacuum(self):
        if random.random() > 0.2:  
            super().vacuum()
    
    def dynamic_dirtying(self):
        for room in self.rooms:
            if random.random() < 0.2:
                self.rooms[room] = 'dirty'


class env_noPositionSensor_deterministic_static(environment):
    def perceive(self):
        return {
            'cleanliness': self.rooms.copy()
        }


class env_noPositionSensor_deterministic_dynamic(environment):
    def perceive(self):
        return {
            'cleanliness': self.rooms.copy()
        }
    
    def dynamic_dirtying(self):
        for room in self.rooms:
            if random.random() < 0.2:
                self.rooms[room] = 'dirty'


class env_noPositionSensor_stochasticInMove_static(environment):
    def perceive(self):
        return {
            'cleanliness': self.rooms.copy()
        }

    def move(self, action):
        if random.random() > 0.2:  
            super().move(action)


class env_noPositionSensor_stochasticInMove_dynamic(environment):
    def perceive(self):
        return {
            'cleanliness': self.rooms.copy()
        }

    def move(self, action):
        if random.random() > 0.2:  
            super().move(action)

    def dynamic_dirtying(self):
        for room in self.rooms:
            if random.random() < 0.2:  
                self.rooms[room] = 'dirty'


class env_noPositionSensor_stochasticInVac_static(environment):
    def perceive(self):
        return {
            'cleanliness': self.rooms.copy()
        }

    def vacuum(self):
        if random.random() > 0.2:  
            super().vacuum()


class env_noPositionSensor_stochasticInVac_dynamic(environment):
    def perceive(self):
        return {
            'cleanliness': self.rooms.copy()
        }

    def vacuum(self):
        if random.random() > 0.2:  
            super().vacuum()

    def dynamic_dirtying(self):
        for room in self.rooms:
            if random.random() < 0.2:  
                self.rooms[room] = 'dirty'


class env_noCleanSensor_deterministic_static(environment):
    def perceive(self):
        return {
            'position': self.robot_position
        }


class env_noCleanSensor_deterministic_dynamic(environment):
    def perceive(self):
        return {
            'position': self.robot_position
        }

    def dynamic_dirtying(self):
        for room in self.rooms:
            if random.random() < 0.2:  
                self.rooms[room] = 'dirty'


class env_noCleanSensor_stochasticInMove_static(environment):
    def perceive(self):
        return {
            'position': self.robot_position
        }

    def move(self, action):
        if random.random() > 0.2:  
            super().move(action)


class env_noCleanSensor_stochasticInMove_dynamic(environment):
    def perceive(self):
        return {
            'position': self.robot_position
        }

    def move(self, action):
        if random.random() > 0.2: 
            super().move(action)

    def dynamic_dirtying(self):
        for room in self.rooms:
            if random.random() < 0.2:  
                self.rooms[room] = 'dirty'


class env_noCleanSensor_stochasticInVac_static(environment):
    def perceive(self):
        return {
            'position': self.robot_position
        }

    def vacuum(self):
        if random.random() > 0.2:  
            super().vacuum()


class env_noCleanSensor_stochasticInVac_dynamic(environment):
    def perceive(self):
        return {
            'position': self.robot_position
        }

    def vacuum(self):
        if random.random() > 0.2: 
            super().vacuum()

    def dynamic_dirtying(self):
        for room in self.rooms:
            if random.random() < 0.2:  
                self.rooms[room] = 'dirty'
