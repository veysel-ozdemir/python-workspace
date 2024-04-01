# Model-View-Controller Pattern

import sqlite3


class DefectModel:
    def getDefectList(self, component):
        query = """select ID from defects where Component = '%s' """ % component
        defectlist = self._dbselect(query)
        list = []
        for row in defectlist:
            list.append(row[0])
        return list

    def getSummary(self, id):
        query = """select summary from defects where ID = '%d' """ % id
        summary = self._dbselect(query)
        for row in summary:
            return row[0]

    def _dbselect(self, query):
        connection = sqlite3.connect("TMS")
        cursorObj = connection.cursor()
        results = cursorObj.execute(query)
        connection.commit()
        cursorObj.close()
        return results


class DefectView:
    def summary(self, summary, defectid):
        print("#### Defect Summary for defect# %d####\n%s" % (defectid, summary))

    def defectList(self, list, category):
        print("#### Defect List for %s ####\n" % category)
        for defect in list:
            print(defect)


class Controller:
    def __init__(self):
        pass

    def getDefectSummary(self, defectid):
        model = DefectModel()
        view = DefectView()
        summary_data = model.getSummary(defectid)
        return view.summary(summary_data, defectid)

    def getDefectList(self, component):
        model = DefectModel()
        view = DefectView()
        defectlist_data = model.getDefectList(component)
        return view.defectList(defectlist_data, component)


controller = Controller()
# Displaying Summary for defect id # 2
print(controller.getDefectSummary(2))
# Displaying defect list for 'ABC' Component
print(controller.getDefectList("ABC"))

# Explanation
# 1. Controller would first get the query from the user. It would know that the query
#   is for viewing defects. Accordingly it would choose DefectModel.
# 2. If the query is for a particular defect, Controller calls getSummary() method of
#   DefectModel, passing the defect id as the argument, for returning the summary
#   of the defect. Then the Controller calls summary() method of DefectView and
#   displays the response to the user.
# 3. If the user query consists of a component name, , Controller calls
#   getDefectList() method of DefectModel, passing the component name as the
#   argument, for returning the defect list for the given component. Then the
#   Controller calls defectList() method of DefectView and displays the response to
#   the user.
