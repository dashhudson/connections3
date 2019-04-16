from http import HTTPStatus

import pytest
from tests.factories import ConnectionFactory

from connections.models.connection import Connection

EXPECTED_FIELDS = [
    'id',
    'from_person',
    'to_person',
    'connection_type',
]

EXPECTED_PERSON_FIELDS = [
    'id',
    'first_name',
    'last_name',
    'email',
]


@pytest.mark.xfail
def test_can_update_connection_type(db, testapp):
    connection = ConnectionFactory(connection_type='friend')
    db.session.commit()
    payload = {
        'connection_type': 'coworker',
    }
    res = testapp.patch(f'/connections/{connection.id}', json=payload)

    assert res.status_code == HTTPStatus.OK

    for field in EXPECTED_FIELDS:
        assert field in res.json
        if field in ['to_person', 'from_person']:
            for p_field in EXPECTED_PERSON_FIELDS:
                assert p_field in res.json[field]

    assert res.json['id'] == connection.id
    assert res.json['connection_type'] == 'coworker'

    updated_connection = Connection.query.get(res.json['id'])

    assert updated_connection is not None
    assert updated_connection.connection_type.value == 'coworker'


@pytest.mark.xfail
def test_update_invalid_connection_type(db, testapp):
    connection = ConnectionFactory(connection_type='friend')
    db.session.commit()
    payload = {
        'connection_type': 'nemesis',
    }
    res = testapp.patch(f'/connections/{connection.id}', json=payload)

    assert res.status_code == HTTPStatus.BAD_REQUEST
    assert res.json['description'] == 'Input failed validation.'
    assert 'connection_type' in res.json['errors']

    unchanged_connection = Connection.query.get(connection.id)

    assert unchanged_connection.connection_type.value == 'friend'


@pytest.mark.xfail
def test_update_connection_not_found(db, testapp):
    payload = {
        'connection_type': 'coworker',
    }
    res = testapp.patch('/connections/999999999999', json=payload)

    assert res.status_code == HTTPStatus.NOT_FOUND
