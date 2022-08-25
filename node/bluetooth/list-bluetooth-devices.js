const si = require('systeminformation');

const checkDeviceName = obj => obj.name.indexOf('Muse') > -1 
si.bluetoothDevices()
.then((devices)=>{
console.log('devices',devices);
if(devices.length > 0){
   console.log(devices.some(checkDeviceName))
}
})
.catch((err)=>console.log('err',err));
