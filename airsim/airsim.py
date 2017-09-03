from PythonClient import *
import time

class Vehicle(AirSimClient):

    VelocityDuration = 1000000

    def __init__(self, ip = ""):
        super().__init__()
        super().confirmConnection()
        super().enableApiControl(True)
        if super().armDisarm(True):
            print('connect succeed!')
        self.homeGps = super().getHomeGeoPoint()  
        self.updateState() 
        self.stateEmergencyChange = False    
        pass
    
    def updateState(self):
        self.position = super().getPosition()
        self.velocity = super().getVelocity()
        self.orientation = super().getOrientation()
        self.slefGPS = super().getGpsLocation()
        self.collision = super().getCollisionInfo()
        self.rollPitchYaw = super().getRollPitchYaw()
    
    def faster(self, accelerate, duration):        
        start = 0.0  
        if duration < 0.1:
            accelerate = accelerate*(duration/0.1)
            duration = 0.1
        while start<duration:
            if self.stateEmergencyChange:
                return
            time.sleep(0.1)
            vx=self.velocity.x_val+accelerate[0]*0.1
            vy=self.velocity.y_val+accelerate[1]*0.1
            vz=self.velocity.z_val+accelerate[2]*0.1
            super().moveByVelocity(vx,vy,vz, Vehicle.VelocityDuration)
            self.updateState()
            # print('the speed is: ',self.velocity.x_val, ' ',vehicle.velocity.y_val,' ', vehicle.velocity.z_val)
            start+=0.1





if __name__ == '__main__':
    vehicle = Vehicle()
    vehicle.goHome()    
    vehicle.moveByVelocityZ(0.5,0,-1, vehicle.VelocityDuration)
    time.sleep(3)
    print('the speed is: ',vehicle.velocity.x_val, ' ',vehicle.velocity.y_val,' ', vehicle.velocity.z_val)
    vehicle.faster((1,2,-1), 1)
    print('the speed is: ',vehicle.velocity.x_val, ' ',vehicle.velocity.y_val,' ', vehicle.velocity.z_val)
    time.sleep(vehicle.VelocityDuration)


        