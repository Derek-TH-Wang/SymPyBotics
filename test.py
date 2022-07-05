import sympy
import sympybotics


# rbtdef = sympybotics.RobotDef('Example Robot', # robot name
#                                 [('-pi/2', 0, 0, 'q+pi/2'),  # list of tuples with Denavit-Hartenberg parameters
#                                 ( 'pi/2', 0, 0, 'q-pi/2')], # (alpha, a, d, theta)
#                                 dh_convention='standard' # either 'standard' or 'modified'
#                             )
# rbtdef.frictionmodel = {'Coulomb', 'viscous'} # options are None or a combination of 'Coulomb', 'viscous' and 'offset'
# rbtdef.gravityacc = sympy.Matrix([0.0, 0.0, -9.81]) # optional, this is the default value

# print(rbtdef.dynparms())


# rbt = sympybotics.RobotDynCode(rbtdef, verbose=True)
# tau_str = sympybotics.robotcodegen.robot_code_to_func('Python', rbt.invdyn_code, 'tau_out', 'tau', rbtdef)
# print(tau_str)


puma560 = sympybotics.RobotDef('puma560', # robot name
                                [('pi/2',  0,      0,      'q'),  # list of tuples with Denavit-Hartenberg parameters
                                ( '0.0',   0.4318, 0,      'q'),
                                ( '-pi/2', 0.0203, 0.1500, 'q'),
                                ( 'pi/2',  0,      0.4318, 'q'),
                                ( '-pi/2', 0,      0,      'q'),
                                ( '0.0',   0,      0,      'q')], # (alpha, a, d, theta)
                                dh_convention='standard' # either 'standard' or 'modified'
                            )
# puma560.frictionmodel = {'Coulomb', 'viscous'} # options are None or a combination of 'Coulomb', 'viscous' and 'offset'
# puma560.frictionmodel = None
puma560.gravityacc = sympy.Matrix([0.0, 0.0, -9.81]) # optional, this is the default value

print(puma560.dynparms())


rbt = sympybotics.RobotDynCode(puma560, verbose=True)
tau_str = sympybotics.robotcodegen.robot_code_to_func('Python', rbt.invdyn_code, 'tau_out', 'tau', puma560)
print(tau_str)



print(rbt.geo.T[-1])