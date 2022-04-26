from db.run_sql import run_sql
from models.biting import Biting
import repositories.human_repository as human_repository
import repositories.zombie_repository as zombie_repository

def save(biting):
    sql = "INSERT INTO bitings ( human_id, zombie_id ) VALUES ( %s, %s) RETURNING id"
    values = [biting.human.id, biting.zombie.id]
    results = run_sql( sql, values)
    biting.id = results[0]['id']
    return biting

def select_all():
    bitings = []

    sql = " SELECT * FROM bitings "
    results = run_sql(sql)

    for row in results:
        human = human_repository.select(row['human_id'])
        zombie = zombie_repository.select(row['zombie'])
        biting = Biting(human, zombie, row['id'])
        bitings.append(biting)
    return bitings

    


def delete_all():
    sql = "DELETE FROM bitings"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM bitings WHERE id = %s"    
    values = [id]
    run_sql(sql, values)


