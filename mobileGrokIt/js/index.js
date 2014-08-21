/*
 *
 */

var TEST_TO_RUN_ON_BATTERY = "readTag";

function postNewUser(inputRFID) {
  var fname = fnames[parseInt(Date.now()) % fnames.length];
  var lname = lnames[parseInt(Date.now()) % lnames.length];
  $.ajax({                                      
      url: "http://184.65.136.142:8080/foresight_api/Users/", 
      type: "POST",
      data: "RFID="+inputRFID+"&password=code&firstName="+fname+"&lastName="+lname,
      dataType: 'json',
      async: true,
      success: function(data)
      {
      }
    });
  return (fname + " " + lname);
}

function ajaxRFID(inputRFID) {
  $.ajax({                                      
      url: "http://184.65.136.142:8080/foresight_api/Users/?format=json&RFID=" + inputRFID, 
      type: "GET",
      data: "",
      dataType: 'json',
      async: true,
      success: function(data)
      {
        if(data.length > 0) {
          //POST TO RECENTLY_SCANNED MODEL
          recentlyScannedPost(inputRFID);
          $('ul').append('<li><a href="#">' + data[0].firstName + ' ' + data[0].lastName + '<br>' + inputRFID +'</a></li>').listview('refresh');
        } else {
          $('ul').append('<li><a href="#">' + postNewUser(inputRFID) + '<br>' + inputRFID + '</a></li>').listview('refresh');
        }
      }
    });
}

function recentlyScannedPost(inputRFID) {
  $.ajax({                                      
    url: "http://184.65.136.142:8080/foresight_api/Recently_Scanned/", 
    type: "POST",
    data: "employeeID=frontDesk&RFID="+inputRFID,
    dataType: 'json',
    async: true,
    success: function(data)
    {
    }
  });
}

function toggleConnected() {
  if(app.started) {
    $("#scanningHeader").text("Now Scanning");
  } else {
    $("#scanningHeader").text("Connected");
  }
}

var scannedRFIDs = [];
var scannedRFIDtimes = [];

var fnames = ['James', 'Liam', 'Terry', 'Mason', 'Drew', 'Antonio', 'Eric', 'Tony', 'Paul', 'Sam', 'Vince'];
var lnames = ['Tyson', 'Lucas', 'Gage', 'Grayson', 'Parker', 'Hunt', 'Baylor', 'Carry', 'Terrace'];

var app = {

started: false,

theTag: null,

inventoryType: 0,

//
// Application Constructor
//
initialize: function() {
  document.addEventListener("deviceready", this.onDeviceReady, false);

  $("#batteryButton").bind("click", function() {
    if (ugi.activeInventory) {
      app[TEST_TO_RUN_ON_BATTERY]();
    } else {
      ugi.getBatteryInfo(function(b) {
        alert("Battery Information\n" +
              b.percentRemaining + "% (" + (b.canScan ? "can scan" : "CANNOT scan") + ")\n" +
              (b.isCharging ? "Charging\n" : "") +
              b.minutesRemaining + " minutes remaining\n" +
              b.voltage + " volts");
      });
    }
  });

  $("#configureButton").bind("click", function() {
    if (app.inventoryType == UgiRfidConfiguration.InventoryTypes.LOCATE_VERY_SHORT_RANGE) {
      app.inventoryType = UgiRfidConfiguration.InventoryTypes.LOCATE_DISTANCE;
    } else {
      app.inventoryType++;
    }
    var config = UgiRfidConfiguration.configWithInventoryType(app.inventoryType);
    alert("RFID Configuration: " + UgiRfidConfiguration.nameForInventoryType(app.inventoryType) + "\n" + config);
  });
  
  $("#startStopButton").bind("click", function() {
		app.started = !app.started;
    toggleConnected();
    if (app.started) {
			$('ul').empty();
      var config = UgiRfidConfiguration.configWithInventoryType(app.inventoryType);
      if (TEST_TO_RUN_ON_BATTERY == "writeTag") {
        config.minUserBytes = config.maxUserBytes = 64;
      }
      //config.selectMask = "35555555";
      //config.selectOffset = 32;
      //config.selectBank = ugi.MemoryBanks.EPC;
      //config.reportRssi = true;
      //config.detailedPerReadData = true;
      config.inventoryVolume = 0;
      config.soundType = 0;
      ugi.startInventory(app, config);
  		$("#startStopButton .ui-btn-text").text("Stop");
		} else {
	  	ugi.activeInventory.stopInventory();
  		$("#startStopButton .ui-btn-text").text("Start");
		}
  });
},

ugiInventoryDidStop: function(result) {
  //ugi.log("ugiInventoryDidStop: " + result);
  if (result != UgiInventoryDelegate.InventoryCompletedReturnValues.LOST_CONNECTION) {
		$("#startStopButton .ui-btn-text").text("Start");
  }
},
ugiInventoryTagFound: function(tag, detailedPerReadData) {
  app.theTag = tag;
  if (detailedPerReadData) {
    ugi.log("ugiInventoryTagFound: " + tag + ", " + (detailedPerReadData ? ", details: " + detailedPerReadData : ""));
  }
  var RFICindex = $.inArray(tag.epc, scannedRFIDs);
  if(RFICindex == -1) {
    ajaxRFID(tag.epc);
    scannedRFIDs = scannedRFIDs + tag.epc;
    scannedRFIDtimes = scannedRFIDtimes + Date.now();
  }
  //alert("RFID = " + tag.epc);
},

////////////////////

/*
ugiInventoryDidStart: function() {
  ugi.log("ugiInventoryDidStart");
},
ugiInventoryTagSubsequentFinds: function(tag, count, detailedPerReadData) {
  ugi.log("ugiInventoryTagSubsequentFinds: " + tag + ", count = " + count + (detailedPerReadData ? ", details: " + detailedPerReadData : ""));
},
ugiInventoryHistoryInterval: function() {
  ugi.log("ugiInventoryHistoryInterval");
},
*/

////////////////////

onDeviceReady: function() {
	ugi.log("------------------------- onDeviceReady: Javascript OK ---------------------------------");
  app.inventoryType = UgiRfidConfiguration.InventoryTypes.LOCATE_DISTANCE;
  ugi.setLogging(ugi.LoggingTypes.STATE /*| ugi.LoggingTypes.INVENTORY*/);
  ugi.openConnection();
  ugi.addConnectionStateCallback(function(connectionState) {
    var isConnected = false;
    if (connectionState == ugi.ConnectionStates.NOT_CONNECTED) {
      $("#infoText").text("Not Connected");
    } else if (connectionState == ugi.ConnectionStates.CONNECTING) {
      $("#infoText").text("Connecting");
    } else if (connectionState == ugi.ConnectionStates.INCOMPATIBLE_READER) {
      $("#infoText").text("Incompatible");
    } else { // connected
      isConnected = true;
    }
    toggleConnected();
    if (isConnected) {
      $("#infoText").hide();
      $("#batteryButton").show();
      $("#configureButton").show();
      $("#scanningHeader").show();
    } else {
      $("#infoText").show();
      $("#batteryButton").hide();
      $("#configureButton").hide();
      $("#scanningHeader").hide();
    }
  });
},

///

programTag: function() {
  if (ugi.activeInventory) {
    if (app.theTag) {
      var epc = app.theTag.epc;
      var newEpc = epc.substring(1) + epc.substring(0, 1);
      alert("About to call ugi.programTag: old epc = " + epc + ", new epc = " + newEpc);
      ugi.activeInventory.programTag(epc, newEpc, UgiInventory.NO_PASSWORD,
                                     function(tag, result) {
                                       alert("Tag Programmed\nresult = " + result + "\ntag = " + tag);
                                     });
    } else alert("No tag");
  } else alert ("Not running inventory");
},

writeTag: function() {
  if (ugi.activeInventory) {
    if (app.theTag) {
      if (app.theTag.userMemory) {
        var newMem = app.theTag.userMemory.substring(2) + app.theTag.userMemory.substring(0, 2);
        alert("About to call ugi.writeTag: epc = " + app.theTag.epc + ", mem = " + newMem);
        ugi.activeInventory.writeTag(app.theTag.epc, ugi.MemoryBanks.USER, 0, newMem,
                                     app.theTag.userMemory, UgiInventory.NO_PASSWORD,
                                     function(tag, result) {
                                       alert("Tag Written\nresult = " + result + "\ntag = " + tag);
                                     });
      } else alert("No user memory read");
    } else alert("No tag");
  } else alert ("Not running inventory");
},

lockUnlockTag: function() {
  if (ugi.activeInventory) {
    if (app.theTag) {
      var maskAndAction = (UgiInventory.LockUnlockMaskAndAction.MASK_CHANGE_WRITABLE <<
                            UgiInventory.LockUnlockMaskAndAction.USER_MASK_BIT_OFFSET) |
                          (UgiInventory.LockUnlockMaskAndAction.ACTION_WRITE_RESTRICTED <<
                            UgiInventory.LockUnlockMaskAndAction.USER_ACTION_BIT_OFFSET);
      alert("About to call lockUnlockTag: epc = " + app.theTag.epc + ", maskAndAction = " + maskAndAction);
        ugi.activeInventory.lockUnlockTag(app.theTag.epc, maskAndAction, UgiInventory.NO_PASSWORD,
                                     function(tag, result) {
                                       alert("Tag Locked/unlocked\nresult = " + result + "\ntag = " + tag);
                                     });
    } else alert("No tag");
  } else alert ("Not running inventory");
},
  
readTag: function() {
  if (ugi.activeInventory) {
    if (app.theTag) {
      ugi.activeInventory.readTag(app.theTag.epc, ugi.MemoryBanks.USER, 0, 32, 1024,
                                  function(tag, data, result) {
                                  alert("Tag Read\nresult = " + result + "\ndata = " + data + "\ntag = " + tag);
                                  });
    } else alert("No tag");
  } else alert ("Not running inventory");
},
  
customCommandToTag: function() {
  if (ugi.activeInventory) {
    if (app.theTag) {
      ugi.activeInventory.customCommandToTag(app.theTag.epc, "e0a9", 16, 72, 8, 250*25,
                                  function(tag, headerBit, data, result) {
                                  alert("Custom command\nresult = " + result +
                                        "\nHeader bit: " + headerBit +
                                        "\ndata = " + data +
                                        "\ntag = " + tag);
                                  });
    } else alert("No tag");
  } else alert ("Not running inventory");
},
  
changePower: function() {
  if (ugi.activeInventory) {
    ugi.activeInventory.changePower(17, 13, 19,
                                  function(success) {
                                    alert("Change power\n" + (success ? "success" : "failure"));
                                  });
  } else alert ("Not running inventory");
}

};
