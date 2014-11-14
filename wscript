## -*- Mode: python; py-indent-offset: 4; indent-tabs-mode: nil; coding: utf-8; -*-

def build(bld):    
    obj = bld.create_ns3_program('vanet-highway-test', ['core'])
    obj.source = [
  'tinyxml.cpp',
  'tinyxmlerror.cpp',
  'tinyxmlparser.cpp',
  'tinystr.cpp',
  'HighwayProject.cc',
	'vanet-highway-test.cc',
  'Geometry.cc',
	'Highway.cc',
	'Vehicle.cc',
	'Obstacle.cc',
	'Model.cc',
	'LaneChange.cc',
  'IdGenerator.cc',
  'TrafficLightGenerator.cc',
  'VehicleGenerator.cc',
	]



