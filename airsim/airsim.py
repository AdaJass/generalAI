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
    
    def accelerate(self, acc, duration):        
        start = 0.0 
        self.updateState()
        startVelocity = self.velocity 
        if duration < 0.1:
            acc = acc*(duration/0.1)
            duration = 0.1
        while start<duration:
            if self.stateEmergencyChange:
                return
            time.sleep(0.1)
            start+=0.1
            vx=startVelocity.x_val+acc[0]*start
            vy=startVelocity.y_val+acc[1]*start
            vz=startVelocity.z_val+acc[2]*start
            super().moveByVelocity(vx,vy,vz, Vehicle.VelocityDuration)
            # print('the speed is: ',self.velocity.x_val, ' ',vehicle.velocity.y_val,' ', vehicle.velocity.z_val)
            


if __name__ == '__main__':
    vehicle = Vehicle()
    vehicle.goHome()    
    vehicle.moveByVelocityZ(0.5,0,-1, vehicle.VelocityDuration)
    time.sleep(3)
    print('the speed is: ',vehicle.velocity.x_val, ' ',vehicle.velocity.y_val,' ', vehicle.velocity.z_val)
    vehicle.faster((1,2,-1), 1)
    print('the speed is: ',vehicle.velocity.x_val, ' ',vehicle.velocity.y_val,' ', vehicle.velocity.z_val)
    time.sleep(vehicle.VelocityDuration)


        