import agents as ag

def HW2Agent() -> object:
    # oldPercepts = [('None', 'Clean','noBott')]
    # oldActions = ['NoOp']
    def program(percept):
        bump, status = percept
        if status == 'Dirty':
            action = 'Suck'
        else:
            lastBump, lastStatus, bottom = program.oldPercepts[-1]
            lastAction = program.oldActions[-1]


            if bprogram.ottom == 'down':
                if bump == 'None':
                    action = 'Down'
                else:
                    program.bottom = 'right'
                    action = 'Right'
            if bottom == 'right':
                if bump =='Bump':
                    action = 'Up'
                    bottom = 'up'
                else:
                    action = 'Left'
            # elif bump == 'Bump':
            #     action = 'Up'
            # else:
            #     action = 'Right'

            #elif lastAction == 'Left' and bump == 'Bump':
            #     leftEdge = 'leftEdge'
            #     action = 'Up'
            # elif leftEdge == 'leftEdge' and lastAction == 'Left' and ceil == 'noCeil':
            #     action = 'Up'
            # elif lastAction == 'Up' and bump == 'Bump':
            #     action = 'Right'
            #     ceil = 'ceil'
            #     leftEdge = 'noLeftEdge'
            # elif lastAction == 'Right' and bump == 'Bump':
            #     rightEdge = 'rightEdge'


        program.oldPercepts.append(percept)
        program.oldActions.append(action)
        return action

    # assign static variables here
    program.oldPercepts = [('None', 'Clean')]
    program.oldActions = ['NoOp']
    program.bottom = 'noBott'

    agt = ag.Agent(program)
    # assign class attributes here:
    # agt.direction = ag.Direction('left')

    return agt