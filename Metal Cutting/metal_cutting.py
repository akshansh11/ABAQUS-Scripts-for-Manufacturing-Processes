# CREATED BY Akshansh Mishra on 09/05/2025 at 12.27 am Central European Summer Time
# This work is licensed under Creative Commons Attribution 4.0 International
# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def Metal_cutting():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=0.1)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.sketchOptions.setValues(decimalPlaces=3)
    s.setPrimaryObject(option=STANDALONE)
    s.Line(point1=(-0.002, 0.012), point2=(-0.002, 0.0))
    s.VerticalConstraint(entity=g[2], addUndoState=False)
    s.Line(point1=(-0.002, 0.0), point2=(-0.01, -0.006))
    s.ObliqueDimension(vertex1=v[1], vertex2=v[2], textPoint=(-0.00273369252681732, 
        -0.00757235940545797), value=0.015)
    s.ObliqueDimension(vertex1=v[0], vertex2=v[1], textPoint=(0.00622240453958511, 
        0.00367221422493458), value=0.02)
    session.viewports['Viewport: 1'].view.fitView()
    s.Line(point1=(-0.014, -0.009), point2=(-0.0095, 0.0175))
    s.AngularDimension(line1=g[3], line2=g[4], textPoint=(-0.0110900569707155, 
        -0.00466267392039299), value=70.0)
    s.unsetPrimaryObject()
    del mdb.models['Model-1'].sketches['__profile__']
    Mdb()
    session.viewports['Viewport: 1'].setValues(displayedObject=None)


def Cutting():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=0.1)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.sketchOptions.setValues(decimalPlaces=3)
    s.setPrimaryObject(option=STANDALONE)
    s.Line(point1=(-0.004, 0.012), point2=(-0.004, -0.00200000004749745))
    s.VerticalConstraint(entity=g[2], addUndoState=False)
    s.Line(point1=(-0.004, -0.00200000004749745), point2=(-0.012, -0.008))
    s.delete(objectList=(g[3], ))
    s.Line(point1=(-0.004, -0.00200000004749745), point2=(-0.014, -0.0055))
    s.ObliqueDimension(vertex1=v[1], vertex2=v[3], textPoint=(-0.00554512813687325, 
        -0.0101290103048086), value=0.015)
    s.ObliqueDimension(vertex1=v[0], vertex2=v[1], textPoint=(0.00484257936477661, 
        0.00436889939010143), value=0.02)
    session.viewports['Viewport: 1'].view.fitView()
    s.Line(point1=(-0.0181578753664579, -0.00695525635851143), point2=(-0.013, 
        0.0165))
    s.AngularDimension(line1=g[5], line2=g[4], textPoint=(-0.0141873992979527, 
        -0.0040852427482605), value=70.0)
    s.Line(point1=(-0.004, 0.0179999999525026), point2=(-0.0279999999664724, 
        0.0179999999525026))
    s.HorizontalConstraint(entity=g[6], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[2], entity2=g[6], addUndoState=False)
    s.ObliqueDimension(vertex1=v[3], vertex2=v[4], textPoint=(-0.02928401902318, 
        0.0052955923601985), value=0.05)
    session.viewports['Viewport: 1'].view.fitView()
    s.autoTrimCurve(curve1=g[6], point1=(-0.0260515902191401, 0.0179415196180344))
    s.autoTrimCurve(curve1=g[5], point1=(-0.0182039942592382, 0.0266281627118587))
    p = mdb.models['Model-1'].Part(name='Tool_Part', dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['Tool_Part']
    p.BaseSolidExtrude(sketch=s, depth=0.02)
    s.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['Tool_Part']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0496341, 
        farPlane=0.0944076, width=0.0566696, height=0.0248427, 
        viewOffsetX=-0.00391807, viewOffsetY=0.00107409)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0483795, 
        farPlane=0.0956622, width=0.0800689, height=0.0351004, 
        viewOffsetX=-0.00950802, viewOffsetY=0.000401693)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0480632, 
        farPlane=0.0959785, width=0.0795456, height=0.034871, 
        viewOffsetX=-0.00219628, viewOffsetY=-0.000622258)
    session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Left'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Right'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Left'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Top'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Bottom'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Top'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Back'])
    session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0548696, 
        farPlane=0.0850281, width=0.0619153, height=0.0271423, 
        viewOffsetX=-0.0013748, viewOffsetY=-0.000321732)
    p1 = mdb.models['Model-1'].parts['Tool_Part']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    mdb.models['Model-1'].parts['Tool_Part'].setValues(space=THREE_D, 
        type=DISCRETE_RIGID_SURFACE)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0536753, 
        farPlane=0.0862224, width=0.0685464, height=0.0300492, 
        viewOffsetX=0.00035269, viewOffsetY=-0.000497665)
    p = mdb.models['Model-1'].parts['Tool_Part']
    c1 = p.cells
    p.RemoveCells(cellList = c1[0:1])
    session.viewports['Viewport: 1'].enableMultipleColors()
    session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
    cmap=session.viewports['Viewport: 1'].colorMappings['Part']
    session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
    session.viewports['Viewport: 1'].disableMultipleColors()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0511722, 
        farPlane=0.0880764, width=0.0653498, height=0.0286479, cameraPosition=(
        -0.057801, 0.00732664, 0.0615882), cameraUpVector=(0.148015, 0.983797, 
        0.101168), cameraTarget=(-0.0108572, 0.00559348, 0.00976046), 
        viewOffsetX=0.000336243, viewOffsetY=-0.000474457)
    p = mdb.models['Model-1'].parts['Tool_Part']
    v1, e, d1, n = p.vertices, p.edges, p.datums, p.nodes
    p.ReferencePoint(point=p.InterestingPoint(edge=e[5], rule=MIDDLE))
    s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=0.1)
    g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
    s1.sketchOptions.setValues(decimalPlaces=3)
    s1.setPrimaryObject(option=STANDALONE)
    s1.rectangle(point1=(-0.012, 0.006), point2=(0.024, 0.0))
    s1.ObliqueDimension(vertex1=v[1], vertex2=v[2], textPoint=(0.00218292325735092, 
        -0.00368549488484859), value=0.08)
    s1.ObliqueDimension(vertex1=v[2], vertex2=v[3], textPoint=(0.027926366776228, 
        0.00212343037128448), value=0.015)
    p = mdb.models['Model-1'].Part(name='Workpiece', dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['Workpiece']
    p.BaseSolidExtrude(sketch=s1, depth=0.018)
    s1.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['Workpiece']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']
    p = mdb.models['Model-1'].parts['Workpiece']
    f, e1, d2 = p.faces, p.edges, p.datums
    t = p.MakeSketchTransform(sketchPlane=f[4], sketchUpEdge=e1[0], 
        sketchPlaneSide=SIDE1, origin=(-0.016, 0.0075, 0.018))
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=0.166, gridSpacing=0.004, transform=t)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.sketchOptions.setValues(decimalPlaces=3)
    s.setPrimaryObject(option=SUPERIMPOSE)
    p = mdb.models['Model-1'].parts['Workpiece']
    p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
    s.Line(point1=(-0.04, 0.004), point2=(0.04, 0.004))
    s.HorizontalConstraint(entity=g[6], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[4], entity2=g[6], addUndoState=False)
    s.CoincidentConstraint(entity1=v[4], entity2=g[4], addUndoState=False)
    s.CoincidentConstraint(entity1=v[5], entity2=g[2], addUndoState=False)
    s.DistanceDimension(entity1=g[5], entity2=g[6], textPoint=(-0.0253161516189575, 
        0.00398024946451187), value=0.004)
    p = mdb.models['Model-1'].parts['Workpiece']
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#10 ]', ), )
    e, d1 = p.edges, p.datums
    p.PartitionFaceBySketch(sketchUpEdge=e[0], faces=pickedFaces, sketch=s)
    s.unsetPrimaryObject()
    del mdb.models['Model-1'].sketches['__profile__']
    p = mdb.models['Model-1'].parts['Workpiece']
    c = p.cells
    pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    e1 = p.edges
    pickedEdges =(e1[0], )
    p.PartitionCellBySweepEdge(sweepPath=e1[7], cells=pickedCells, 
        edges=pickedEdges)
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
    a = mdb.models['Model-1'].rootAssembly
    a.DatumCsysByDefault(CARTESIAN)
    p = mdb.models['Model-1'].parts['Tool_Part']
    a.Instance(name='Tool_Part-1', part=p, dependent=ON)
    p = mdb.models['Model-1'].parts['Workpiece']
    a.Instance(name='Workpiece-1', part=p, dependent=ON)
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['Workpiece-1'].edges
    a.DatumPointByMidPoint(point1=a.instances['Workpiece-1'].InterestingPoint(
        edge=e1[14], rule=MIDDLE), 
        point2=a.instances['Workpiece-1'].InterestingPoint(edge=e1[3], 
        rule=MIDDLE))
    a1 = mdb.models['Model-1'].rootAssembly
    a1.translate(instanceList=('Tool_Part-1', ), vector=(0.042158, 0.019955, 
        -0.001))
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
        engineeringFeatures=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
    p = mdb.models['Model-1'].parts['Workpiece']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    mdb.models['Model-1'].Material(name='Material-1')
    mdb.models['Model-1'].materials['Material-1'].JohnsonCookDamageInitiation(
        table=((0.071, 1.248, -1.142, 0.147, 0.1, 933.0, 373.0, 1.0), ))
    mdb.models['Model-1'].materials['Material-1'].johnsonCookDamageInitiation.DamageEvolution(
        type=DISPLACEMENT, table=((1e-05, ), ))
    mdb.models['Model-1'].materials['Material-1'].Density(table=((2700.0, ), ))
    mdb.models['Model-1'].materials['Material-1'].Elastic(table=((70000000000.0, 
        0.27), ))
    mdb.models['Model-1'].materials['Material-1'].Plastic(hardening=JOHNSON_COOK, 
        scaleStress=None, table=((148000000.0, 341000000.0, 0.183, 0.859, 
        933.0, 373.0), ))
    mdb.models['Model-1'].materials['Material-1'].plastic.RateDependent(
        type=JOHNSON_COOK, table=((0.001, 1.0), ))
    mdb.models['Model-1'].HomogeneousSolidSection(name='Section-1', 
        material='Material-1', thickness=None)
    p = mdb.models['Model-1'].parts['Workpiece']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#3 ]', ), )
    region = p.Set(cells=cells, name='Set-1')
    p = mdb.models['Model-1'].parts['Workpiece']
    p.SectionAssignment(region=region, sectionName='Section-1', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)
    session.viewports['Viewport: 1'].enableMultipleColors()
    session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
    cmap=session.viewports['Viewport: 1'].colorMappings['Property']
    session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
    session.viewports['Viewport: 1'].disableMultipleColors()
    a1 = mdb.models['Model-1'].rootAssembly
    a1.regenerate()
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        adaptiveMeshConstraints=ON)
    mdb.models['Model-1'].ExplicitDynamicsStep(name='Step-1', previous='Initial', 
        scaleFactor=1.0, massScaling=((SEMI_AUTOMATIC, MODEL, AT_BEGINNING, 
        0.0, 0.0001, BELOW_MIN, 0, 0, 0.0, 0.0, 0, None), ), 
        improvedDtMethod=ON)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
    mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValues(variables=(
        'S', 'SVAVG', 'PE', 'PEVAVG', 'PEEQ', 'PEEQVAVG', 'LE', 'U', 'V', 'A', 
        'RF', 'CSTRESS', 'EVF', 'STATUS'))
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
        constraints=ON, connectors=ON, engineeringFeatures=ON, 
        adaptiveMeshConstraints=OFF)
    session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, 
        interactions=OFF, constraints=OFF, connectors=OFF, 
        engineeringFeatures=OFF)
    session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
        meshTechnique=ON)
    p = mdb.models['Model-1'].parts['Workpiece']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
        engineeringFeatures=OFF, mesh=ON)
    session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
        meshTechnique=ON)
    p = mdb.models['Model-1'].parts['Workpiece']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#8000 ]', ), )
    p.seedEdgeByNumber(edges=pickedEdges, number=15, constraint=FINER)
    session.viewports['Viewport: 1'].partDisplay.setValues(renderStyle=SHADED)
    session.viewports['Viewport: 1'].setColor(globalTranslucency=True)
    p = mdb.models['Model-1'].parts['Workpiece']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#80025 ]', ), )
    p.seedEdgeByNumber(edges=pickedEdges, number=150, constraint=FINER)
    p = mdb.models['Model-1'].parts['Workpiece']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#1490a ]', ), )
    p.seedEdgeByNumber(edges=pickedEdges, number=1, constraint=FINER)
    p = mdb.models['Model-1'].parts['Workpiece']
    p.generateMesh()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.140983, 
        farPlane=0.225099, width=0.102474, height=0.0450357, 
        viewOffsetX=0.00133469, viewOffsetY=0.000823459)
    session.viewports['Viewport: 1'].setColor(globalTranslucency=False)
    elemType1 = mesh.ElemType(elemCode=C3D8R, elemLibrary=EXPLICIT, 
        kinematicSplit=AVERAGE_STRAIN, secondOrderAccuracy=OFF, 
        hourglassControl=DEFAULT, distortionControl=DEFAULT, elemDeletion=ON)
    elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=EXPLICIT)
    elemType3 = mesh.ElemType(elemCode=C3D4, elemLibrary=EXPLICIT)
    p = mdb.models['Model-1'].parts['Workpiece']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#3 ]', ), )
    pickedRegions =(cells, )
    p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, 
        elemType3))
    p = mdb.models['Model-1'].parts['Tool_Part']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    p = mdb.models['Model-1'].parts['Tool_Part']
    p.seedPart(size=0.0025, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Model-1'].parts['Tool_Part']
    p.generateMesh()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0529991, 
        farPlane=0.0891101, width=0.0678937, height=0.0298381, 
        viewOffsetX=0.000229805, viewOffsetY=0.000442523)
    elemType1 = mesh.ElemType(elemCode=R3D4, elemLibrary=EXPLICIT)
    elemType2 = mesh.ElemType(elemCode=R3D3, elemLibrary=EXPLICIT)
    p = mdb.models['Model-1'].parts['Tool_Part']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#3f ]', ), )
    pickedRegions =(faces, )
    p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2))
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    a1 = mdb.models['Model-1'].rootAssembly
    a1.regenerate()
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF, 
        interactions=ON, constraints=ON, connectors=ON, engineeringFeatures=ON)
    session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
        meshTechnique=OFF)
    session.viewports['Viewport: 1'].view.setValues(session.views['Back'])
    session.viewports['Viewport: 1'].view.setProjection(projection=PARALLEL)
    session.linkedViewportCommands.setValues(_highlightLinkedViewports=False)
    i1 = mdb.models['Model-1'].rootAssembly.allInstances['Tool_Part-1']
    leaf = dgm.LeafFromInstance(instances=(i1, ))
    session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
        leaf=leaf)
    mdb.models['Model-1'].ContactProperty('IntProp-1')
    mdb.models['Model-1'].interactionProperties['IntProp-1'].TangentialBehavior(
        formulation=PENALTY, directionality=ISOTROPIC, slipRateDependency=OFF, 
        pressureDependency=OFF, temperatureDependency=OFF, dependencies=0, 
        table=((0.2, ), ), shearStressLimit=None, maximumElasticSlip=FRACTION, 
        fraction=0.005, elasticSlipStiffness=None)
    mdb.models['Model-1'].interactionProperties['IntProp-1'].NormalBehavior(
        pressureOverclosure=HARD, allowSeparation=ON, 
        constraintEnforcementMethod=DEFAULT)
    a = mdb.models['Model-1'].rootAssembly
    s1 = a.instances['Tool_Part-1'].faces
    side1Faces1 = s1.getSequenceFromMask(mask=('[#3f ]', ), )
    a.Surface(side1Faces=side1Faces1, name='Surf-1')
    session.linkedViewportCommands.setValues(_highlightLinkedViewports=False)
    i1 = mdb.models['Model-1'].rootAssembly.allInstances['Workpiece-1']
    leaf = dgm.LeafFromInstance(instances=(i1, ))
    session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
        leaf=leaf)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
    a = mdb.models['Model-1'].rootAssembly
    n1 = a.instances['Workpiece-1'].nodes
    nodes1 = n1.getSequenceFromMask(mask=(
        '[#f00 #0:18 #f7fffffe #fffff9ff #ffffffff:9 #bffefffb #fbffefff', 
        ' #ffbffeff #fffbffef #efffbffe #fefffbff #ffefffbf #bffefffb #fbffefff', 
        ' #ffbffeff #fffbffef #efffbffe #fefffbff #ffefffbf #bffefffb #fbffefff', 
        ' #ffbffeff #fffbffef #efffbffe #fefffbff #ffefffbf #bffefffb #fbffefff', 
        ' #ffbffeff #fffbffef #efffbffe #fefffbff #ffefffbf #bffefffb #fbffefff', 
        ' #ffbffeff #fffbffef #efffbffe #fefffbff #ffefffbf #bffefffb #fbffefff', 
        ' #ffbffeff #fffbffef #efffbffe #fefffbff #ffefffbf #bffefffb #fbffefff', 
        ' #ffbffeff #fffbffef #efffbffe #fefffbff #ffefffbf #bffefffb #fbffefff', 
        ' #ffbffeff #fffbffef #efffbffe #fefffbff #ffefffbf #bffefffb #fbffefff', 
        ' #ffbffeff #fffbffef #efffbffe #fefffbff #ffefffbf #bffefffb #fbffefff', 
        ' #ffbffeff #fffbffef #efffbffe #fefffbff #ffefffbf #bffefffb #fbffefff', 
        ' #ffbffeff #fffbffef #efffbffe #fefffbff #ffefffbf #bffefffb #fbffefff', 
        ' #ffbffeff #fffbffef #efffbffe #fefffbff #ffefffbf #bffefffb #fbffefff', 
        ' #ffbffeff #fffbffef #efffbffe #fefffbff #ffefffbf #bffefffb #fbffefff', 
        ' #ffbffeff #fffbffef #efffbffe #fefffbff #ffefffbf #bffefffb #fbffefff', 
        ' #ffbffeff #fffbffef #efffbffe #fefffbff #ffefffbf #bffefffb #fbffefff', 
        ' #ffbffeff #fffbffef #efffbffe #fefffbff #ffefffbf #bffefffb #fbffefff', 
        ' #ffbffeff #fffbffef #efffbffe #fefffbff #ffefffbf #bffefffb #fbffefff', 
        ' #ffbffeff #fffbffef #efffbffe #fefffbff #ffefffbf #bffefffb #fbffefff', 
        ' #ffbffeff #fffbffef #3ffe ]', ), )
    a.Set(nodes=nodes1, name='Set-1')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
    a = mdb.models['Model-1'].rootAssembly
    region1=a.surfaces['Surf-1']
    a = mdb.models['Model-1'].rootAssembly
    region2=a.sets['Set-1']
    mdb.models['Model-1'].SurfaceToSurfaceContactExp(name ='Int-1', 
        createStepName='Step-1', main = region1, secondary = region2, 
        mechanicalConstraint=KINEMATIC, sliding=FINITE, 
        interactionProperty='IntProp-1', initialClearance=OMIT, datumAxis=None, 
        clearanceRegion=None)
    session.linkedViewportCommands.setValues(_highlightLinkedViewports=False)
    leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
    session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
        leaf=leaf)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
        predefinedFields=ON, interactions=OFF, constraints=OFF, 
        engineeringFeatures=OFF)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
    a = mdb.models['Model-1'].rootAssembly
    c1 = a.instances['Workpiece-1'].cells
    cells1 = c1.getSequenceFromMask(mask=('[#1 ]', ), )
    region = a.Set(cells=cells1, name='Set-2')
    mdb.models['Model-1'].EncastreBC(name='BC-1', createStepName='Initial', 
        region=region, localCsys=None)
    session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
    a = mdb.models['Model-1'].rootAssembly
    r1 = a.instances['Tool_Part-1'].referencePoints
    refPoints1=(r1[3], )
    region = a.Set(referencePoints=refPoints1, name='Set-3')
    mdb.models['Model-1'].DisplacementBC(name='BC-2', createStepName='Initial', 
        region=region, u1=UNSET, u2=SET, u3=SET, ur1=SET, ur2=SET, ur3=SET, 
        amplitude=UNSET, distributionType=UNIFORM, fieldName='', 
        localCsys=None)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
    mdb.models['Model-1'].TabularAmplitude(name='Amp-1', timeSpan=STEP, 
        smooth=SOLVER_DEFAULT, data=((0.0, 0.0), (1.0, 1.0)))
    mdb.models['Model-1'].boundaryConditions['BC-2'].setValuesInStep(
        stepName='Step-1', u1=-0.08, amplitude='Amp-1')
    session.viewports['Viewport: 1'].view.setProjection(projection=PERSPECTIVE)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
        predefinedFields=OFF, connectors=OFF)
    mdb.Job(name='job_cutting', model='Model-1', description='', type=ANALYSIS, 
        atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
        memoryUnits=PERCENTAGE, explicitPrecision=SINGLE, 
        nodalOutputPrecision=SINGLE, echoPrint=OFF, modelPrint=OFF, 
        contactPrint=OFF, historyPrint=OFF, userSubroutine='', scratch='', 
        resultsFormat=ODB, numDomains=1, activateLoadBalancing=False, 
        numThreadsPerMpiProcess=1, multiprocessingMode=DEFAULT, numCpus=1)
    mdb.jobs['job_cutting'].submit(consistencyChecking=OFF)
    session.mdbData.summary()
    o3 = session.openOdb(name='Y:/job_cutting.odb')
    session.viewports['Viewport: 1'].setValues(displayedObject=o3)
    session.viewports['Viewport: 1'].makeCurrent()


