from pymongo import MongoClient
client = MongoClient('10.111.12.43', 27017)
db = client.test_qt
# myjs="db.kd_car.find()"
# myjs="function(){return db.getCollectionNames()}"
myjs='''db.ttms_order.find({created:{$gte:1552233600},source:2}).forEach(function(order){
  var projectId = order.projectId;
  db.ttms_project.find({_id:ObjectId(projectId),$where: "this.warehouseAddressList.length == 1"}).forEach(function(project){
    db.ttms_order.update({_id:ObjectId(order._id.str)},
    {$set:
      {"consigner.address.lng":project.warehouseAddressList[0].lng,
       "consigner.address.lat":project.warehouseAddressList[0].lat,
       "consigner.address.province":project.warehouseAddressList[0].province,
       "consigner.address.city":project.warehouseAddressList[0].city,
       "consigner.address.address":project.warehouseAddressList[0].address
      }
    })
  });
})'''
print(db.eval(myjs))