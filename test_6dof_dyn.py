import math



def fkine(q):
    q1 = q[0]
    q2 = q[1]
    q3 = q[2]
    q4 = q[3]
    q5 = q[4]
    q6 = q[5]

    T = [[(((-math.sin(q2)*math.sin(q3)*math.cos(q1) + math.cos(q1)*math.cos(q2)*math.cos(q3))*math.cos(q4) - math.sin(q1)*math.sin(q4))*math.cos(q5) + (-math.sin(q2)*math.cos(q1)*math.cos(q3) - math.sin(q3)*math.cos(q1)*math.cos(q2))*math.sin(q5))*math.cos(q6) + (-(-math.sin(q2)*math.sin(q3)*math.cos(q1) + math.cos(q1)*math.cos(q2)*math.cos(q3))*math.sin(q4) - math.sin(q1)*math.cos(q4))*math.sin(q6), 
    -(((-math.sin(q2)*math.sin(q3)*math.cos(q1) + math.cos(q1)*math.cos(q2)*math.cos(q3))*math.cos(q4) - math.sin(q1)*math.sin(q4))*math.cos(q5) + (-math.sin(q2)*math.cos(q1)*math.cos(q3) - math.sin(q3)*math.cos(q1)*math.cos(q2))*math.sin(q5))*math.sin(q6) + (-(-math.sin(q2)*math.sin(q3)*math.cos(q1) + math.cos(q1)*math.cos(q2)*math.cos(q3))*math.sin(q4) - math.sin(q1)*math.cos(q4))*math.cos(q6), 
    -((-math.sin(q2)*math.sin(q3)*math.cos(q1) + math.cos(q1)*math.cos(q2)*math.cos(q3))*math.cos(q4) - math.sin(q1)*math.sin(q4))*math.sin(q5) + (-math.sin(q2)*math.cos(q1)*math.cos(q3) - math.sin(q3)*math.cos(q1)*math.cos(q2))*math.cos(q5), 
    0.15*math.sin(q1) - 0.0203*math.sin(q2)*math.sin(q3)*math.cos(q1) - 0.4318*math.sin(q2)*math.cos(q1)*math.cos(q3) - 0.4318*math.sin(q3)*math.cos(q1)*math.cos(q2) + 0.0203*math.cos(q1)*math.cos(q2)*math.cos(q3) + 0.4318*math.cos(q1)*math.cos(q2)], 
    [(((-math.sin(q1)*math.sin(q2)*math.sin(q3) + math.sin(q1)*math.cos(q2)*math.cos(q3))*math.cos(q4) + math.sin(q4)*math.cos(q1))*math.cos(q5) + (-math.sin(q1)*math.sin(q2)*math.cos(q3) - math.sin(q1)*math.sin(q3)*math.cos(q2))*math.sin(q5))*math.cos(q6) + (-(-math.sin(q1)*math.sin(q2)*math.sin(q3) + math.sin(q1)*math.cos(q2)*math.cos(q3))*math.sin(q4) + math.cos(q1)*math.cos(q4))*math.sin(q6), 
    -(((-math.sin(q1)*math.sin(q2)*math.sin(q3) + math.sin(q1)*math.cos(q2)*math.cos(q3))*math.cos(q4) + math.sin(q4)*math.cos(q1))*math.cos(q5) + (-math.sin(q1)*math.sin(q2)*math.cos(q3) - math.sin(q1)*math.sin(q3)*math.cos(q2))*math.sin(q5))*math.sin(q6) + (-(-math.sin(q1)*math.sin(q2)*math.sin(q3) + math.sin(q1)*math.cos(q2)*math.cos(q3))*math.sin(q4) + math.cos(q1)*math.cos(q4))*math.cos(q6), 
    -((-math.sin(q1)*math.sin(q2)*math.sin(q3) + math.sin(q1)*math.cos(q2)*math.cos(q3))*math.cos(q4) + math.sin(q4)*math.cos(q1))*math.sin(q5) + (-math.sin(q1)*math.sin(q2)*math.cos(q3) - math.sin(q1)*math.sin(q3)*math.cos(q2))*math.cos(q5), 
    -0.0203*math.sin(q1)*math.sin(q2)*math.sin(q3) - 0.4318*math.sin(q1)*math.sin(q2)*math.cos(q3) - 0.4318*math.sin(q1)*math.sin(q3)*math.cos(q2) + 0.0203*math.sin(q1)*math.cos(q2)*math.cos(q3) + 0.4318*math.sin(q1)*math.cos(q2) - 0.15*math.cos(q1)], 
    [((-math.sin(q2)*math.sin(q3) + math.cos(q2)*math.cos(q3))*math.sin(q5) + (math.sin(q2)*math.cos(q3) + math.sin(q3)*math.cos(q2))*math.cos(q4)*math.cos(q5))*math.cos(q6) - (math.sin(q2)*math.cos(q3) + math.sin(q3)*math.cos(q2))*math.sin(q4)*math.sin(q6), 
    -((-math.sin(q2)*math.sin(q3) + math.cos(q2)*math.cos(q3))*math.sin(q5) + (math.sin(q2)*math.cos(q3) + math.sin(q3)*math.cos(q2))*math.cos(q4)*math.cos(q5))*math.sin(q6) - (math.sin(q2)*math.cos(q3) + math.sin(q3)*math.cos(q2))*math.sin(q4)*math.cos(q6), 
    (-math.sin(q2)*math.sin(q3) + math.cos(q2)*math.cos(q3))*math.cos(q5) - (math.sin(q2)*math.cos(q3) + math.sin(q3)*math.cos(q2))*math.sin(q5)*math.cos(q4), 
    -0.4318*math.sin(q2)*math.sin(q3) + 0.0203*math.sin(q2)*math.cos(q3) + 0.4318*math.sin(q2) + 0.0203*math.sin(q3)*math.cos(q2) + 0.4318*math.cos(q2)*math.cos(q3) + 0.6718], 
    [0, 0, 0, 1]]

    return T

def cal_tau(parms, q, dq, ddq):
#
    tau_out = [0]*6
#
    x0 = math.sin(q[1])
    x1 = math.cos(q[1])
    x2 = dq[0]*x1
    x3 = ddq[0]*x0 + dq[1]*x2
    x4 = ddq[0]*x1
    x5 = dq[0]*x0
    x6 = -dq[1]
    x7 = x4 + x5*x6
    x8 = -0.4318*x0**2 - 0.4318*x1**2
    x9 = 0.4318*dq[1]
    x10 = x4*x8 + x5*x9
    x11 = x2*x8
    x12 = -x2
    x13 = parms[18]*x12 + parms[19]*x5 + parms[21]*x11
    x14 = dq[1]*parms[17] + parms[14]*x5 + parms[16]*x2 + parms[18]*x9
    x15 = math.cos(q[2])
    x16 = x15*x3
    x17 = math.sin(q[2])
    x18 = x17*x7
    x19 = x15*x2
    x20 = x17*x5
    x21 = -x20
    x22 = x19 + x21
    x23 = -dq[2]
    x24 = -x23
    x25 = x16 + x18 + x22*x24
    x26 = -ddq[1] - ddq[2]
    x27 = x15*x7
    x28 = x17*x3
    x29 = -x28
    x30 = x15*x5
    x31 = x17*x2
    x32 = x30 + x31
    x33 = x23*x32 + x27 + x29
    x34 = 0.0203*x15**2 + 0.0203*x17**2
    x35 = 0.4318*ddq[1] + 9.81*x1
    x36 = 9.81*x0
    x37 = -x17
    x38 = x17*x9 + 0.15*x19 - 0.15*x20
    x39 = ddq[1]*x34 + 0.0203*ddq[2] + x15*x35 - 0.15*x16 - 0.15*x18 + x23*x38 + x36*x37
    x40 = math.cos(q[3])
    x41 = x25*x40
    x42 = math.sin(q[3])
    x43 = x26*x42
    x44 = x32*x42
    x45 = x23 + x6
    x46 = x40*x45
    x47 = x44 - x46
    x48 = -dq[3]
    x49 = x41 + x43 + x47*x48
    x50 = ddq[3] + x33
    x51 = x25*x42
    x52 = -x40
    x53 = x32*x40
    x54 = x42*x45
    x55 = x53 + x54
    x56 = dq[3]*x55 + x26*x52 + x51
    x57 = 0.0203*dq[2]
    x58 = dq[1]*x34 + x15*x9 - 0.15*x30 - 0.15*x31
    x59 = x15*x36 + x17*x35 + x24*x58 + 0.15*x27 - 0.15*x28 + x57*x6
    x60 = -x10
    x61 = -x32
    x62 = x27*x34 + x29*x34 + x57*x61 + x60
    x63 = -x11
    x64 = x19*x34 + x21*x34 + x63
    x65 = x38*x40 + x42*x64 - 0.4318*x44 + 0.4318*x46
    x66 = dq[3]*x65 + 0.4318*x41 + x42*x59 + 0.4318*x43 + x52*x62
    x67 = dq[3] + x22
    x68 = x57 + x58
    x69 = -x65
    x70 = parms[38]*x55 + parms[40]*x67 + parms[41]*x47 + parms[42]*x68 + parms[43]*x69
    x71 = math.cos(q[4])
    x72 = math.sin(q[4])
    x73 = -x72
    x74 = x55*x73 + x67*x71
    x75 = -dq[4]
    x76 = -x75
    x77 = x49*x71 + x50*x72 + x74*x76
    x78 = -x56
    x79 = -ddq[4] + x78
    x80 = x55*x71 + x67*x72
    x81 = x49*x73 + x50*x71 + x75*x80
    x82 = 0.4318*x40
    x83 = x38*x42 + x52*x64 + 0.4318*x53 + 0.4318*x54
    x84 = x26*x82 + x40*x59 + x42*x62 + x48*x83 - 0.4318*x51
    x85 = x65*x71 + x68*x72
    x86 = x39*x71 + x73*x84 + x75*x85
    x87 = -x83
    x88 = x65*x73 + x68*x71
    x89 = -x47
    x90 = x75 + x89
    x91 = -parms[54]
    x92 = parms[55]*x80 + parms[57]*x88 + x90*x91
    x93 = -parms[55]
    x94 = parms[50]*x80 + parms[52]*x90 + parms[53]*x74 + parms[54]*x87 + x85*x93
    x95 = math.cos(q[5])
    x96 = math.sin(q[5])
    x97 = -x96
    x98 = x80*x97 + x90*x95
    x99 = dq[5]*x98 + x77*x95 + x79*x96
    x100 = x80*x95 + x90*x96
    x101 = -dq[5]
    x102 = x100*x101 + x77*x97 + x79*x95
    x103 = ddq[5] + x81
    x104 = dq[5] + x74
    x105 = x85*x97 + x87*x95
    x106 = x85*x95 + x87*x96
    x107 = -parms[67]
    x108 = parms[62]*x100 + parms[64]*x98 + parms[65]*x104 + parms[66]*x105 + x106*x107
    x109 = -parms[66]
    x110 = parms[67]*x100 + parms[69]*x88 + x109*x98
    x111 = -x66
    x112 = x39*x72 + x71*x84 + x76*x88
    x113 = x101*x106 + x111*x95 + x112*x97
    x114 = -parms[68]
    x115 = parms[66]*x104 + parms[69]*x105 + x100*x114
    x116 = -x115
    x117 = parms[61]*x100 + parms[63]*x98 + parms[64]*x104 + parms[68]*x106 + x109*x88
    x118 = parms[60]*x99 + parms[61]*x102 + parms[62]*x103 + parms[67]*x86 - x104*x117 + x105*x110 + x108*x98 + x113*x114 + x116*x88
    x119 = -parms[56]
    x120 = parms[49]*x80 + parms[51]*x90 + parms[52]*x74 + parms[56]*x85 + x88*x91
    x121 = -x74
    x122 = parms[54]*x74 + parms[57]*x87 + x119*x80
    x123 = dq[5]*x105 + x111*x96 + x112*x95
    x124 = parms[68]*x98 + parms[69]*x106 + x104*x107
    x125 = parms[60]*x100 + parms[61]*x98 + parms[62]*x104 + parms[67]*x88 + x105*x114
    x126 = -x100
    x127 = parms[61]*x99 + parms[63]*x102 + parms[64]*x103 + parms[68]*x123 + x104*x125 - x106*x110 + x108*x126 + x109*x86 + x124*x88
    x128 = parms[48]*x77 + parms[49]*x79 + parms[50]*x81 + parms[55]*x86 + x111*x119 + x118*x95 + x120*x121 - x122*x88 + x127*x97 + x87*x92 + x90*x94
    x129 = -x67
    x130 = parms[42]*x129 + parms[43]*x55 + parms[45]*x83
    x131 = -parms[44]
    x132 = parms[37]*x55 + parms[39]*x67 + parms[40]*x47 + parms[42]*x87 + parms[44]*x65
    x133 = parms[42]*x47 + parms[45]*x68 + x131*x55
    x134 = -x98
    x135 = parms[62]*x99 + parms[64]*x102 + parms[65]*x103 + parms[66]*x113 + x100*x117 - x105*x124 + x106*x115 + x107*x123 + x125*x134
    x136 = parms[56]*x90 + parms[57]*x85 + x74*x93
    x137 = -x136
    x138 = parms[48]*x80 + parms[49]*x90 + parms[50]*x74 + parms[55]*x88 + x119*x87
    x139 = parms[50]*x77 + parms[52]*x79 + parms[53]*x81 + parms[54]*x111 + x112*x93 + x120*x80 + x122*x85 + x135 + x137*x87 - x138*x90
    x140 = parms[36]*x49 + parms[37]*x50 + parms[38]*x56 + parms[43]*x66 + x128*x71 + x130*x68 + x131*x39 + x132*x89 + x133*x87 + x139*x73 + x67*x70
    x141 = -parms[30]
    x142 = parms[31]*x32 + parms[33]*x68 + x141*x45
    x143 = -x80
    x144 = -parms[49]*x77 - parms[51]*x79 - parms[52]*x81 - parms[56]*x112 - x118*x96 - x127*x95 - x136*x88 - x138*x74 - x143*x94 + x85*x92 - x86*x91
    x145 = parms[36]*x55 + parms[37]*x67 + parms[38]*x47 + parms[43]*x83 + x131*x68
    x146 = parms[43]*x89 + parms[44]*x67 + parms[45]*x65
    x147 = -x68
    x148 = parms[38]*x49 + parms[40]*x50 + parms[41]*x56 + parms[42]*x39 - parms[43]*x84 + x129*x145 + x132*x55 + x133*x65 + x144 + x146*x147
    x149 = -parms[31]
    x150 = parms[26]*x32 + parms[28]*x45 + parms[29]*x22 + parms[30]*x64 + x149*x38
    x151 = -parms[32]
    x152 = parms[25]*x32 + parms[27]*x45 + parms[28]*x22 + parms[30]*x147 + parms[32]*x38
    x153 = -x22
    x154 = parms[30]*x22 + parms[32]*x61 + parms[33]*x64
    x155 = parms[68]*x102 + parms[69]*x123 + x103*x107 + x104*x116 + x110*x98
    x156 = parms[66]*x103 + parms[69]*x113 + x104*x124 + x110*x126 + x114*x99
    x157 = -parms[42]*x50 + parms[43]*x49 + parms[45]*x66 - parms[54]*x81 - parms[57]*x111 - x119*x77 + x129*x146 + x133*x55 - x136*x74 - x143*x92 - x155*x96 - x156*x95
    x158 = parms[56]*x79 + parms[57]*x112 + x121*x122 + x155*x95 + x156*x97 + x81*x93 + x90*x92
    x159 = parms[55]*x77 + parms[57]*x86 + parms[67]*x99 + parms[69]*x86 + x100*x115 + x102*x109 + x122*x80 + x124*x134 + x137*x90 + x79*x91
    x160 = parms[43]*x78 + parms[44]*x50 + parms[45]*x84 + x130*x67 + x133*x89 + x158*x71 + x159*x73
    x161 = x160*x42
    x162 = parms[24]*x25 + parms[25]*x26 + parms[26]*x33 + parms[31]*x39 + x140*x40 + x142*x64 + x147*x154 + x148*x42 + x150*x45 + x151*x62 + x152*x153 + x157*x82 - 0.4318*x161
    x163 = dq[1]*parms[16] + parms[13]*x5 + parms[15]*x2 + parms[18]*x63
    x164 = -parms[20]
    x165 = -x55
    x166 = parms[37]*x49 + parms[39]*x50 + parms[40]*x56 + parms[42]*x111 + parms[44]*x84 + x128*x72 + x130*x69 + x139*x71 + x145*x47 + x146*x83 + x165*x70
    x167 = parms[32]*x45 + parms[33]*x38 + x149*x22
    x168 = -x167
    x169 = parms[24]*x32 + parms[25]*x45 + parms[26]*x22 + parms[31]*x68 + x151*x64
    x170 = parms[26]*x25 + parms[28]*x26 + parms[29]*x33 + parms[30]*x62 + x149*x59 + x152*x32 + x154*x38 + x166 + x168*x64 - x169*x45
    x171 = dq[1]*parms[18] + parms[21]*x9 + x164*x5
    x172 = x157*x42
    x173 = parms[32]*x26 + parms[33]*x59 + x142*x45 + x149*x33 + x153*x154 + x160*x40 + x172
    x174 = -0.15*x17
    x175 = parms[31]*x25 + parms[33]*x39 + parms[42]*x56 + parms[45]*x39 + x130*x165 + x131*x49 + x141*x26 + x146*x47 + x154*x32 + x158*x72 + x159*x71 + x168*x45
    x176 = x15*x175
    x177 = parms[30]*x33 + parms[33]*x62 + x142*x61 + x151*x25 + x157*x52 + x161 + x167*x22
    x178 = x177*x34
    x179 = dq[1]*parms[14] + parms[12]*x5 + parms[13]*x2 + parms[19]*x11 + x164*x9
    x180 = parms[19]*x6 + parms[20]*x2
    x181 = -x5
    x182 = -parms[25]*x25 - parms[27]*x26 - parms[28]*x33 - parms[32]*x59 - x140*x42 - x141*x39 + x142*x38 - x148*x52 - x150*x61 - x160*x82 - x167*x68 - x169*x22 - 0.4318*x172
#
    tau_out[0] = ddq[0]*parms[3] + dq[0]*parms[10] + parms[11]*(0.0 if dq[0] == 0 else math.copysign(1, dq[0])) + x0*(ddq[1]*parms[14] + parms[12]*x3 + parms[13]*x7 + parms[19]*x10 + x13*x9 + x14*x2 + x15*x162 + x163*x6 + x164*x35 + x170*x37 + x171*x63 + x173*x174 - 0.15*x176 + x178*x37) + x1*x8*(-parms[18]*x7 + parms[19]*x3 + parms[21]*x10 + x12*x180 + x171*x5 - x177) + x1*(ddq[1]*parms[16] + dq[1]*x179 + parms[13]*x3 + parms[15]*x7 + parms[18]*x60 + parms[20]*x36 + x11*x180 + x14*x181 + x15*x170 + 0.15*x15*x173 + x15*x178 + x162*x17 + x174*x175)
    tau_out[1] = ddq[1]*parms[17] + 0.4318*ddq[1]*parms[18] + dq[1]*parms[22] + 0.4318*dq[1]*x180 + parms[14]*x3 + parms[16]*x7 + parms[18]*x35 - parms[19]*x36 + 0.4318*parms[21]*x35 + parms[23]*(0.0 if dq[1] == 0 else math.copysign(1, dq[1])) + x12*x179 + 0.4318*x13*x181 + x163*x5 + 0.4318*x164*x3 + 0.4318*x17*x173 + x175*x34 + 0.4318*x176 - x180*x9 + x182
    tau_out[2] = dq[2]*parms[34] + parms[35]*(0.0 if dq[2] == 0 else math.copysign(1, dq[2])) + 0.0203*x175 + x182
    tau_out[3] = dq[3]*parms[46] + parms[47]*(0.0 if dq[3] == 0 else math.copysign(1, dq[3])) + x166
    tau_out[4] = dq[4]*parms[58] + parms[59]*(0.0 if dq[4] == 0 else math.copysign(1, dq[4])) + x144
    tau_out[5] = dq[5]*parms[70] + parms[71]*(0.0 if dq[5] == 0 else math.copysign(1, dq[5])) + x135
#
    return tau_out


def cal_tau_nofric(parms, q, dq, ddq):
#
    tau_out = [0]*6
#
    x0 = math.sin(q[1])
    x1 = math.cos(q[1])
    x2 = dq[0]*x1
    x3 = ddq[0]*x0 + dq[1]*x2
    x4 = ddq[0]*x1
    x5 = dq[0]*x0
    x6 = -dq[1]
    x7 = x4 + x5*x6
    x8 = -0.4318*x0**2 - 0.4318*x1**2
    x9 = 0.4318*dq[1]
    x10 = x4*x8 + x5*x9
    x11 = x2*x8
    x12 = -x2
    x13 = parms[16]*x12 + parms[17]*x5 + parms[19]*x11
    x14 = dq[1]*parms[15] + parms[12]*x5 + parms[14]*x2 + parms[16]*x9
    x15 = math.cos(q[2])
    x16 = x15*x3
    x17 = math.sin(q[2])
    x18 = x17*x7
    x19 = x15*x2
    x20 = x17*x5
    x21 = -x20
    x22 = x19 + x21
    x23 = -dq[2]
    x24 = -x23
    x25 = x16 + x18 + x22*x24
    x26 = -ddq[1] - ddq[2]
    x27 = x15*x7
    x28 = x17*x3
    x29 = -x28
    x30 = x15*x5
    x31 = x17*x2
    x32 = x30 + x31
    x33 = x23*x32 + x27 + x29
    x34 = 0.0203*x15**2 + 0.0203*x17**2
    x35 = 0.4318*ddq[1] + 9.81*x1
    x36 = 9.81*x0
    x37 = -x17
    x38 = x17*x9 + 0.15*x19 - 0.15*x20
    x39 = ddq[1]*x34 + 0.0203*ddq[2] + x15*x35 - 0.15*x16 - 0.15*x18 + x23*x38 + x36*x37
    x40 = math.cos(q[3])
    x41 = x25*x40
    x42 = math.sin(q[3])
    x43 = x26*x42
    x44 = x32*x42
    x45 = x23 + x6
    x46 = x40*x45
    x47 = x44 - x46
    x48 = -dq[3]
    x49 = x41 + x43 + x47*x48
    x50 = ddq[3] + x33
    x51 = x25*x42
    x52 = -x40
    x53 = x32*x40
    x54 = x42*x45
    x55 = x53 + x54
    x56 = dq[3]*x55 + x26*x52 + x51
    x57 = 0.0203*dq[2]
    x58 = dq[1]*x34 + x15*x9 - 0.15*x30 - 0.15*x31
    x59 = x15*x36 + x17*x35 + x24*x58 + 0.15*x27 - 0.15*x28 + x57*x6
    x60 = -x10
    x61 = -x32
    x62 = x27*x34 + x29*x34 + x57*x61 + x60
    x63 = -x11
    x64 = x19*x34 + x21*x34 + x63
    x65 = x38*x40 + x42*x64 - 0.4318*x44 + 0.4318*x46
    x66 = dq[3]*x65 + 0.4318*x41 + x42*x59 + 0.4318*x43 + x52*x62
    x67 = dq[3] + x22
    x68 = x57 + x58
    x69 = -x65
    x70 = parms[32]*x55 + parms[34]*x67 + parms[35]*x47 + parms[36]*x68 + parms[37]*x69
    x71 = math.cos(q[4])
    x72 = math.sin(q[4])
    x73 = -x72
    x74 = x55*x73 + x67*x71
    x75 = -dq[4]
    x76 = -x75
    x77 = x49*x71 + x50*x72 + x74*x76
    x78 = -x56
    x79 = -ddq[4] + x78
    x80 = x55*x71 + x67*x72
    x81 = x49*x73 + x50*x71 + x75*x80
    x82 = 0.4318*x40
    x83 = x38*x42 + x52*x64 + 0.4318*x53 + 0.4318*x54
    x84 = x26*x82 + x40*x59 + x42*x62 + x48*x83 - 0.4318*x51
    x85 = x65*x71 + x68*x72
    x86 = x39*x71 + x73*x84 + x75*x85
    x87 = -x83
    x88 = x65*x73 + x68*x71
    x89 = -x47
    x90 = x75 + x89
    x91 = -parms[46]
    x92 = parms[47]*x80 + parms[49]*x88 + x90*x91
    x93 = -parms[47]
    x94 = parms[42]*x80 + parms[44]*x90 + parms[45]*x74 + parms[46]*x87 + x85*x93
    x95 = math.cos(q[5])
    x96 = math.sin(q[5])
    x97 = -x96
    x98 = x80*x97 + x90*x95
    x99 = dq[5]*x98 + x77*x95 + x79*x96
    x100 = x80*x95 + x90*x96
    x101 = -dq[5]
    x102 = x100*x101 + x77*x97 + x79*x95
    x103 = ddq[5] + x81
    x104 = dq[5] + x74
    x105 = x85*x97 + x87*x95
    x106 = x85*x95 + x87*x96
    x107 = -parms[57]
    x108 = parms[52]*x100 + parms[54]*x98 + parms[55]*x104 + parms[56]*x105 + x106*x107
    x109 = -parms[56]
    x110 = parms[57]*x100 + parms[59]*x88 + x109*x98
    x111 = -x66
    x112 = x39*x72 + x71*x84 + x76*x88
    x113 = x101*x106 + x111*x95 + x112*x97
    x114 = -parms[58]
    x115 = parms[56]*x104 + parms[59]*x105 + x100*x114
    x116 = -x115
    x117 = parms[51]*x100 + parms[53]*x98 + parms[54]*x104 + parms[58]*x106 + x109*x88
    x118 = parms[50]*x99 + parms[51]*x102 + parms[52]*x103 + parms[57]*x86 - x104*x117 + x105*x110 + x108*x98 + x113*x114 + x116*x88
    x119 = -parms[48]
    x120 = parms[41]*x80 + parms[43]*x90 + parms[44]*x74 + parms[48]*x85 + x88*x91
    x121 = -x74
    x122 = parms[46]*x74 + parms[49]*x87 + x119*x80
    x123 = dq[5]*x105 + x111*x96 + x112*x95
    x124 = parms[58]*x98 + parms[59]*x106 + x104*x107
    x125 = parms[50]*x100 + parms[51]*x98 + parms[52]*x104 + parms[57]*x88 + x105*x114
    x126 = -x100
    x127 = parms[51]*x99 + parms[53]*x102 + parms[54]*x103 + parms[58]*x123 + x104*x125 - x106*x110 + x108*x126 + x109*x86 + x124*x88
    x128 = parms[40]*x77 + parms[41]*x79 + parms[42]*x81 + parms[47]*x86 + x111*x119 + x118*x95 + x120*x121 - x122*x88 + x127*x97 + x87*x92 + x90*x94
    x129 = -x67
    x130 = parms[36]*x129 + parms[37]*x55 + parms[39]*x83
    x131 = -parms[38]
    x132 = parms[31]*x55 + parms[33]*x67 + parms[34]*x47 + parms[36]*x87 + parms[38]*x65
    x133 = parms[36]*x47 + parms[39]*x68 + x131*x55
    x134 = -x98
    x135 = parms[52]*x99 + parms[54]*x102 + parms[55]*x103 + parms[56]*x113 + x100*x117 - x105*x124 + x106*x115 + x107*x123 + x125*x134
    x136 = parms[48]*x90 + parms[49]*x85 + x74*x93
    x137 = -x136
    x138 = parms[40]*x80 + parms[41]*x90 + parms[42]*x74 + parms[47]*x88 + x119*x87
    x139 = parms[42]*x77 + parms[44]*x79 + parms[45]*x81 + parms[46]*x111 + x112*x93 + x120*x80 + x122*x85 + x135 + x137*x87 - x138*x90
    x140 = parms[30]*x49 + parms[31]*x50 + parms[32]*x56 + parms[37]*x66 + x128*x71 + x130*x68 + x131*x39 + x132*x89 + x133*x87 + x139*x73 + x67*x70
    x141 = -parms[26]
    x142 = parms[27]*x32 + parms[29]*x68 + x141*x45
    x143 = -x80
    x144 = -parms[41]*x77 - parms[43]*x79 - parms[44]*x81 - parms[48]*x112 - x118*x96 - x127*x95 - x136*x88 - x138*x74 - x143*x94 + x85*x92 - x86*x91
    x145 = parms[30]*x55 + parms[31]*x67 + parms[32]*x47 + parms[37]*x83 + x131*x68
    x146 = parms[37]*x89 + parms[38]*x67 + parms[39]*x65
    x147 = -x68
    x148 = parms[32]*x49 + parms[34]*x50 + parms[35]*x56 + parms[36]*x39 - parms[37]*x84 + x129*x145 + x132*x55 + x133*x65 + x144 + x146*x147
    x149 = -parms[27]
    x150 = parms[22]*x32 + parms[24]*x45 + parms[25]*x22 + parms[26]*x64 + x149*x38
    x151 = -parms[28]
    x152 = parms[21]*x32 + parms[23]*x45 + parms[24]*x22 + parms[26]*x147 + parms[28]*x38
    x153 = -x22
    x154 = parms[26]*x22 + parms[28]*x61 + parms[29]*x64
    x155 = parms[58]*x102 + parms[59]*x123 + x103*x107 + x104*x116 + x110*x98
    x156 = parms[56]*x103 + parms[59]*x113 + x104*x124 + x110*x126 + x114*x99
    x157 = -parms[36]*x50 + parms[37]*x49 + parms[39]*x66 - parms[46]*x81 - parms[49]*x111 - x119*x77 + x129*x146 + x133*x55 - x136*x74 - x143*x92 - x155*x96 - x156*x95
    x158 = parms[48]*x79 + parms[49]*x112 + x121*x122 + x155*x95 + x156*x97 + x81*x93 + x90*x92
    x159 = parms[47]*x77 + parms[49]*x86 + parms[57]*x99 + parms[59]*x86 + x100*x115 + x102*x109 + x122*x80 + x124*x134 + x137*x90 + x79*x91
    x160 = parms[37]*x78 + parms[38]*x50 + parms[39]*x84 + x130*x67 + x133*x89 + x158*x71 + x159*x73
    x161 = x160*x42
    x162 = parms[20]*x25 + parms[21]*x26 + parms[22]*x33 + parms[27]*x39 + x140*x40 + x142*x64 + x147*x154 + x148*x42 + x150*x45 + x151*x62 + x152*x153 + x157*x82 - 0.4318*x161
    x163 = dq[1]*parms[14] + parms[11]*x5 + parms[13]*x2 + parms[16]*x63
    x164 = -parms[18]
    x165 = -x55
    x166 = parms[31]*x49 + parms[33]*x50 + parms[34]*x56 + parms[36]*x111 + parms[38]*x84 + x128*x72 + x130*x69 + x139*x71 + x145*x47 + x146*x83 + x165*x70
    x167 = parms[28]*x45 + parms[29]*x38 + x149*x22
    x168 = -x167
    x169 = parms[20]*x32 + parms[21]*x45 + parms[22]*x22 + parms[27]*x68 + x151*x64
    x170 = parms[22]*x25 + parms[24]*x26 + parms[25]*x33 + parms[26]*x62 + x149*x59 + x152*x32 + x154*x38 + x166 + x168*x64 - x169*x45
    x171 = dq[1]*parms[16] + parms[19]*x9 + x164*x5
    x172 = x157*x42
    x173 = parms[28]*x26 + parms[29]*x59 + x142*x45 + x149*x33 + x153*x154 + x160*x40 + x172
    x174 = -0.15*x17
    x175 = parms[27]*x25 + parms[29]*x39 + parms[36]*x56 + parms[39]*x39 + x130*x165 + x131*x49 + x141*x26 + x146*x47 + x154*x32 + x158*x72 + x159*x71 + x168*x45
    x176 = x15*x175
    x177 = parms[26]*x33 + parms[29]*x62 + x142*x61 + x151*x25 + x157*x52 + x161 + x167*x22
    x178 = x177*x34
    x179 = dq[1]*parms[12] + parms[10]*x5 + parms[11]*x2 + parms[17]*x11 + x164*x9
    x180 = parms[17]*x6 + parms[18]*x2
    x181 = -x5
    x182 = -parms[21]*x25 - parms[23]*x26 - parms[24]*x33 - parms[28]*x59 - x140*x42 - x141*x39 + x142*x38 - x148*x52 - x150*x61 - x160*x82 - x167*x68 - x169*x22 - 0.4318*x172
#
    tau_out[0] = ddq[0]*parms[3] + x0*(ddq[1]*parms[12] + parms[10]*x3 + parms[11]*x7 + parms[17]*x10 + x13*x9 + x14*x2 + x15*x162 + x163*x6 + x164*x35 + x170*x37 + x171*x63 + x173*x174 - 0.15*x176 + x178*x37) + x1*x8*(-parms[16]*x7 + parms[17]*x3 + parms[19]*x10 + x12*x180 + x171*x5 - x177) + x1*(ddq[1]*parms[14] + dq[1]*x179 + parms[11]*x3 + parms[13]*x7 + parms[16]*x60 + parms[18]*x36 + x11*x180 + x14*x181 + x15*x170 + 0.15*x15*x173 + x15*x178 + x162*x17 + x174*x175)
    tau_out[1] = ddq[1]*parms[15] + 0.4318*ddq[1]*parms[16] + 0.4318*dq[1]*x180 + parms[12]*x3 + parms[14]*x7 + parms[16]*x35 - parms[17]*x36 + 0.4318*parms[19]*x35 + x12*x179 + 0.4318*x13*x181 + x163*x5 + 0.4318*x164*x3 + 0.4318*x17*x173 + x175*x34 + 0.4318*x176 - x180*x9 + x182
    tau_out[2] = 0.0203*x175 + x182
    tau_out[3] = x166
    tau_out[4] = x144
    tau_out[5] = x135
#
    return tau_out

# parm = [L_1xx, L_1xy, L_1xz, L_1yy, L_1yz, L_1zz, l_1x, l_1y, l_1z, m_1, fv_1, fc_1, 
#         L_2xx, L_2xy, L_2xz, L_2yy, L_2yz, L_2zz, l_2x, l_2y, l_2z, m_2, fv_2, fc_2, 
#         L_3xx, L_3xy, L_3xz, L_3yy, L_3yz, L_3zz, l_3x, l_3y, l_3z, m_3, fv_3, fc_3, 
#         L_4xx, L_4xy, L_4xz, L_4yy, L_4yz, L_4zz, l_4x, l_4y, l_4z, m_4, fv_4, fc_4, 
#         L_5xx, L_5xy, L_5xz, L_5yy, L_5yz, L_5zz, l_5x, l_5y, l_5z, m_5, fv_5, fc_5, 
#         L_6xx, L_6xy, L_6xz, L_6yy, L_6yz, L_6zz, l_6x, l_6y, l_6z, m_6, fv_6, fc_6]

# L1 = [0, 0, 0, 0.35, 0, 0, 0, 0, 0, 0, 0, 0]
# L2 = [0.13, 0, 0, 0.524, 0, 0.539, -0.3638, 0.006, 0.2275, 17.4, 0, 0]
# L3 = [0.066, 0, 0, 0.086, 0, 0.0125, -0.0203, -0.0141, 0.070, 4.8, 0, 0]
# L4 = [1.8e-3, 0, 0, 1.3e-3, 0, 1.8e-3, 0, 0.019, 0, 0.82, 0, 0]
# L5 = [0.3e-3, 0, 0, 0.4e-3, 0, 0.3e-3, 0, 0, 0, 0.34, 0, 0]
# L6 = [0.15e-3, 0, 0, 0.15e-3, 0, 0.04e-3, 0, 0, 0.032, 0.09, 0, 0]
# params = L1+L2+L3+L4+L5+L6
dynparm = [0.0, -0, -0, 0.35, -0, 0.0, 0.0, 0.0, 0.0, 0, 0, 0, 
            1.03118515, 0.037980719999999996, 1.4401022999999999, 3.7274564059999999, -0.023751000000000001, 2.8425240559999998, -6.33012, 0.10439999999999999, 3.9585, 17.4, 0, 0,
            0.090474288000000014, -0.0013739039999999998, 0.0068208000000000001, 0.111498032, 0.0047375999999999998, 0, 0,
            0.015432319999999999, -0.09743999999999998, -0.06767999999999999, 0.336, 4.8, 0.0020960200000000001, -0, -0, 0, 0,
            0.0012999999999999999, -0, 0.0020960200000000001, 0.0, 0.015579999999999998, 0.0, 0.82, 0.00029999999999999997, -0, -0, 0, 0,
            0.00040000000000000002, -0, 0.00029999999999999997, 0.0, 0.0, 0.0, 0.34, 0.00024216, -0, -0, 0.00024216, -0, 0, 0,
            4.0000000000000003e-05, 0.0, 0.0, 0.0028799999999999997, 0.09, 0, 0]
dynparm1 = [0.0, -0, -0, 0.35, -0, 0.0, 0.0, 0.0, 0.0, 0,
            1.03118515, 0.037980719999999996, 1.4401022999999999, 3.7274564059999999, -0.023751000000000001, 2.8425240559999998, -6.33012, 0.10439999999999999, 3.9585, 17.4,
            0.090474288000000014, -0.0013739039999999998, 0.0068208000000000001, 0.111498032, 0.0047375999999999998,
            0.015432319999999999, -0.09743999999999998, -0.06767999999999999, 0.336, 4.8, 0.0020960200000000001, -0, -0,
            0.0012999999999999999, -0, 0.0020960200000000001, 0.0, 0.015579999999999998, 0.0, 0.82, 0.00029999999999999997, -0, -0,
            0.00040000000000000002, -0, 0.00029999999999999997, 0.0, 0.0, 0.0, 0.34, 0.00024216, -0, -0, 0.00024216, -0,
            4.0000000000000003e-05, 0.0, 0.0, 0.0028799999999999997, 0.09]
# print(params)
qn = [0, math.pi / 4, math.pi, 0, math.pi / 4, 0]
qr = [0, math.pi / 2, -math.pi / 2, 0, 0, 0]
q0 = [0, 0, 0, 0, 0, 0]
qd = [0, 0, 0, 0, 0, 0]
qdd = [0, 0, 0, 0, 0, 0]

q = q0

tau = cal_tau(dynparm, q, qd, qdd)
print("tau = ", tau)

#no friction is right with robotics-toolbox-python
tau = cal_tau_nofric(dynparm1, q, qd, qdd)
print("tau_nofric = ", tau)

T = fkine(q)
print("T = ", T)