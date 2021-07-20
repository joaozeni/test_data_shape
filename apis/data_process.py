import json
from flask import Blueprint, request, jsonify
from sqlalchemy import func, extract, and_
from apis.models.equipment import equipment
from apis.models.failure import failure
from apis.models.sensor import sensor
from apis.models.model import db


data_process_blueprint = Blueprint('data_process', __name__)


@data_process_blueprint.route('/total_failures', methods=['GET'])
def total_failure():

    """Returns the total failures in the system
        ---
        responses:
          200:
            description: a label total with the total in a int
    """
    query = db.session.query(func.count(failure.id).label('total'))
    query_results = db.session.execute(query)
    total = query_results.all()[0][0]
    return {'total':total}, 200


@data_process_blueprint.route('/most_failure_equipment', methods=['GET'])
def most_failure():

    """Return the code of the equipment with most failure and the total failures(could return failures by equipment too)
        ---
        responses:
          200:
            description: return the code of the equipment in the key code, the total of failures in the key failures
    """
    query = db.session.query(func.count(equipment.code).label('failures'), equipment.code).join(failure, equipment.id==failure.equipment_id).group_by(equipment.code).order_by(db.desc('failures'))
    query_results = db.session.execute(query)
    most_failure = query_results.all()[0]
    code = most_failure[1]
    failures = most_failure[0]
    return {'code': code, 'failures': failures}, 200


@data_process_blueprint.route('/avg_failures_by_group', methods=['GET'])
def avg_failures_by_group():

    """Returns the average failures by group
        ---
        responses:
          200:
            description: returns a result label with a list, in each element containg the following labels group_code(the code name of the group) group_failures(the total failures of that group)  group_equipments(the total equipments of that group) group_avg(the average failures of the group being group_failures/group_equipments)
    """
    # This query is somehow complex, its based in a subquery, so the first part of the query returns the numeber of equipments in
    # a group, the joins this query with one counting the number of failures in a group
    query_equipment_count = db.session.query(equipment.group_name.label('e_id'), func.count('*').label('equipments_in_group')).group_by(equipment.group_name).subquery('equipment_count')
    query = db.session.query(equipment.group_name, func.count().label('total_failure'), query_equipment_count.c.equipments_in_group).join(failure, equipment.id==failure.equipment_id).join(query_equipment_count, query_equipment_count.c.e_id==equipment.group_name).group_by(equipment.group_name, query_equipment_count.c.equipments_in_group).order_by('total_failure')
    query_results = db.session.execute(query)
    result_list = []
    for row in query_results:
        result = {'group_code': row[0], 'group_failures':row[1], 'group_equipments':row[2], 'group_avg':row[1]/row[2]}
        result_list.append(result)
    return {'results': result_list}, 200

