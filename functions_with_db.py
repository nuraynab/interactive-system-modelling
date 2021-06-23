import MySQLdb as mdb
from contextlib import closing

db = mdb.connect('127.0.0.1', 'root', '', 'interSys')


def get_sem_mem(version_id):
    sem_mem = {}
    with closing(db.cursor()) as cur:
        cur.execute("SELECT * FROM sem_mem WHERE version_id = '%i' ORDER BY id" % version_id)
        fact_repr = cur.fetchall()

        for y in fact_repr:
            sem_mem[y[3]] = [y[2], y[4], y[5], y[6], y[7]]
    return sem_mem


def get_env(version_id):
    env = {}
    with closing(db.cursor()) as cur:
        cur.execute("SELECT * FROM environment WHERE version_id = '%i' ORDER BY id" % version_id)
        perc_repr = cur.fetchall()

        for y in perc_repr:
            env[y[4]] = [y[2], y[3], y[5], y[6], y[7], y[8]]
    return env


def get_exp(version_id):
    exp = {}
    with closing(db.cursor()) as cur:
        cur.execute("SELECT * FROM experiment WHERE version_id = '%i' ORDER BY id" % (version_id))
        perc_repr = cur.fetchall()

        for y in perc_repr:
            exp[y[4]] = [y[2], y[3], y[6], y[7], y[8], y[9], y[5], y[10], y[11]]
    return exp


def get_domains(version_id):
    with closing(db.cursor()) as cur:
        cur.execute("SELECT * FROM domains WHERE version_id = '%i'" % (version_id))
        domains = cur.fetchall()
    return domains


def get_categories(version_id):
    with closing(db.cursor()) as cur:
        cur.execute("SELECT * FROM categories WHERE version_id = '%i'" % (version_id))
        categories = cur.fetchall()
    return categories


def get_types(version_id):
    with closing(db.cursor()) as cur:
        cur.execute("SELECT * FROM types WHERE version_id = '%i'" % (version_id))
        types = cur.fetchall()
    return types


def get_attributes(version_id):
    with closing(db.cursor()) as cur:
        cur.execute("SELECT * FROM attributes WHERE version_id = '%i'" % (version_id))
        attributes = cur.fetchall()
    return attributes


def get_facts(version_id):
    with closing(db.cursor()) as cur:
        cur.execute("SELECT * FROM facts WHERE version_id = '%i'" % (version_id))
        facts = cur.fetchall()
    return facts


def get_fact(version_id, cur_fact):
    with closing(db.cursor()) as cur:
        cur.execute("SELECT * FROM facts WHERE version_id = '%i' AND value = '%s'" % (version_id, cur_fact))
        facts = cur.fetchall()
    return facts


def add_fact_to_exp(params):
    with closing(db.cursor()) as cur:
        cur.execute(
            "INSERT INTO experiment(version_id, domain, item, value, future_time, persist_time, categories, types, "
            "attributes, repeat_num, in_time) "
            "VALUES('%i', '%s', 'fact', '%s', '%i', '%i', '%s', '%s', '%s', '%i', '%i')" % (
                params[0], params[1], params[2], params[3],
                params[4], params[5], params[6], params[7], params[8], params[9]))
        db.commit()


def add_fact_to_stm(params):
    with closing(db.cursor()) as cur:
        cur.execute(
            "INSERT INTO short_term_mem(version_id, domain, item, value, decay, categories, types, attributes)"
            "VALUES('%i', '%s', 'fact', '%s', '%i', '%s', '%s', '%s')" % (params[0], params[1], params[2], params[3],
                                                                          params[4], params[5], params[6]))
        db.commit()


def add_fact_to_env(params):
    with closing(db.cursor()) as cur:
        cur.execute(
            "INSERT INTO environment(version_id, domain, item, value, persist_time, categories, types, attributes)"
            "VALUES('%i', '%s', 'fact', '%s', '%i', '%s', '%s', '%s')" % (params[0], params[1], params[2], params[3],
                                                                          params[4], params[5], params[6]))
        db.commit()


def get_questions(version_id):
    with closing(db.cursor()) as cur:
        cur.execute("SELECT * FROM questions WHERE version_id = '%i'" % (version_id))
        questions = cur.fetchall()
    return questions


def get_question(version_id, cur_quest):
    with closing(db.cursor()) as cur:
        cur.execute("SELECT * FROM questions WHERE version_id = '%i' AND value = '%s'" % (version_id, cur_quest))
        questions = cur.fetchall()
    return questions


def add_quest_to_exp(params):
    with closing(db.cursor()) as cur:
        cur.execute(
            "INSERT INTO experiment(version_id, domain, item, value, future_time, persist_time, categories, types, "
            "attributes, repeat_num, in_time) VALUES('%i', '%s', 'question', '%s', '%i', '%i', '%s', '%s', '%s', "
            "NULL, NULL)" % (params[0], params[1], params[2], params[3], params[4], params[5], params[6], params[7]))
        db.commit()


def add_quest_to_stm(params):
    with closing(db.cursor()) as cur:
        cur.execute(
            "INSERT INTO short_term_mem(version_id, domain, item, value, decay, categories, types, attributes)"
            "VALUES('%i', '%s', 'question', '%s', '%i', '%s', '%s', '%s')" % (params[0], params[1], params[2], params[3],
                                                                              params[4], params[5], params[6]))
        db.commit()


def add_quest_to_env(params):
    with closing(db.cursor()) as cur:
        cur.execute(
            "INSERT INTO environment(version_id, domain, item, value, persist_time, categories, types, attributes)"
            "VALUES('%i', '%s', 'question', '%s', '%i', '%s', '%s', '%s')" % (params[0], params[1], params[2], params[3],
                                                                              params[4], params[5], params[6]))
        db.commit()


def get_fact_or_quest_by_value(item, version_id, value):
    with closing(db.cursor()) as cur:
        cur.execute("SELECT * FROM %s WHERE version_id = '%i' AND value = '%s'" % (item, version_id, value))
        items = cur.fetchall()
    return items


def edit_fact_in_component(params):
    with closing(db.cursor()) as cur:
        cur.execute(
            "UPDATE experiment SET domain = '%s', value = '%s', future_time = '%i', persist_time = '%i', repeat_num = "
            "'%i', in_time = '%i', categories = '%s', types = '%s', attributes = '%s' WHERE version_id = '%i' AND "
            "domain = '%s' AND value = '%s' "
            % (params[0], params[1], params[2], params[3],
            params[4], params[5], params[6], params[7], params[8], params[9], params[10], params[11]))
        db.commit()


def edit_quest_in_component(params):
    with closing(db.cursor()) as cur:
        cur.execute(
            "UPDATE experiment SET domain = '%s', value = '%s', future_time = '%i', persist_time = '%i', categories = '%s', "
            "types = '%s', attributes = '%s' WHERE version_id = '%i' AND domain = '%s' AND value = '%s'"
            % (params[0], params[1], params[2], params[3],
            params[4], params[5], params[6], params[7], params[8], params[9]))
        db.commit()


def edit_item_in_env(params):
    with closing(db.cursor()) as cur:
        cur.execute(
            "UPDATE environment SET domain = '%s', value = '%s', persist_time = '%i', categories = '%s', types = '%s', "
            "attributes = '%s' WHERE version_id = '%i' AND domain = '%s' AND value = '%s'"
            % (params[0], params[1], params[2], params[3], params[4], params[5], params[6], params[7], params[8]))
        db.commit()


def edit_item_in_stm(params):
    with closing(db.cursor()) as cur:
        cur.execute(
            "UPDATE short_term_mem SET domain = '%s', value = '%s', decay = '%i', categories = '%s', "
            "types = '%s', attributes = '%s' WHERE version_id = '%i' AND domain = '%s' AND value = '%s'"
            % (params[0], params[1], params[2], params[3], params[4], params[5], params[6], params[7], params[8]))
        db.commit()