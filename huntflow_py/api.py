from huntflow_py.client import Client


class BaseAPI(object):
    """Common API methods and params."""

    # TODO mock for testing purposes?
    URL = 'https://api.huntflow.ru/'

    def __init__(self, token=None, email=None):
        self.token = token

        self.client = Client(token=token, email=email)
        self.client.BASE_URL = self.URL


class APIv1(BaseAPI):
    """
    API version 1.

    Sadly, Huntflow does not actually version their API, so this is "first" version as of 23.04.2020.

    Guys, if you read this, take a look at SemVer or something. :)
    """

    def __init__(self, **kwargs):
        super(APIv1, self).__init__(**kwargs)

    # User info and accounts list
    # https://github.com/huntflow/api/blob/master/ru/user.md

    def me(self):
        """Curent user information."""
        return self.client._request('/me')

    def accounts(self):
        """Organizations available to user."""
        return self.client._request('/accounts')

    # Directories
    # https://github.com/huntflow/api/blob/master/ru/dicts.md

    def vacancy_statuses_by_account(self, account_id):
        """Stages of headhunting."""
        return self.client._request(f'/account/{account_id}/vacancy/statuses')

    def applicant_sources_by_account(self, account_id):
        """Sources of applicants."""
        return self.client._request(f'/account/{account_id}/applicant/sources')

    # File uploading
    # https://github.com/huntflow/api/blob/master/ru/upload.md

    def file_upload(self, account_id, file_path):
        """File upload."""
        return self.client._request(
            f'/account/{account_id}/upload',
            method='POST',
            headers={
                'X-File-Parse': True
            },
            files={
                'file': file_path
            }
        )

    # Vacancy applications
    # https://github.com/huntflow/api/blob/master/ru/vacancy_requests.md

    def vacancy_request_schemas(self, account_id):
        """List of schemas for vacancy request."""
        return self.client._request(f'/account/{account_id}/account_vacancy_request')

    def vacancy_request_schema_by_vacancy_request(self, account_id, account_vacancy_request_id):
        """Schema for specific vacancy request."""
        return self.client._request(f'/account/{account_id}/account_vacancy_request/{account_vacancy_request_id}')

    def vacancy_requests(self, account_id, vacancy_id=None):
        """List of vacancy requests.

        Supports stating `vacancy_id` which filters list by selected vacancy.
        """

        return self.client._request(
            f'/account/{account_id}/account_vacancy_request',
            params={'vacancy_id': vacancy_id} if vacancy_id else {}
        )

    def vacancy_requests_by_vacancy(self, account_id, vacancy_id):
        """List of vacancy requests filtered by selected vacancy."""
        return self.vacancy_requests(account_id, vacancy_id=vacancy_id)

    def vacancy_request(self, account_id, vacancy_request_id):
        """Vacancy request."""
        return self.client._request(f'/account/{account_id}/vacancy_request/{vacancy_request_id}')

    def vacancy_request_create(self, account_id, payload={}):
        """Create vacancy request."""
        return self.client._request(
            f'/account/{account_id}/vacancy_request',
            method='POST',
            json=payload
        )

    # Vacancies
    # https://github.com/huntflow/api/blob/master/ru/vacancies.md

    # TODO implement vacancies methods

    # Candidates
    # https://github.com/huntflow/api/blob/master/ru/applicants.md

    # TODO implement applicants methods

    def applicants(self, account_id, **kwargs):
        """List of applicants."""
        return self.client._request(f'/account/{account_id}/applicants', **kwargs)

    # Resumes
    # https://github.com/huntflow/api/blob/master/ru/externals.md

    # TODO implement externals methods

    def resume_info(self, account_id, applicant_id, external_id):
        """Get applicant's resume."""
        return self.client._request(f'/account/{account_id}/applicants/{applicant_id}/external/{external_id}')

    external = resume_info

    # Questionaries
    # https://github.com/huntflow/api/blob/master/ru/questionaries.md

    # TODO implement questionaries methods

    # Tags
    # https://github.com/huntflow/api/blob/master/ru/tags.md

    def tags_by_account(self, account_id):
        """Company's tags."""
        # TODO Is pagination possible here?
        return self.client._request(f'/account/{account_id}/tag')

    def tag_info(self, account_id, tag_id):
        """Tag info."""
        return self.client._request(f'/account/{account_id}/tag/{tag_id}')

    def tag_create(self, account_id, payload={}):
        """Tag info."""
        return self.client._request(
            f'/account/{account_id}/tag',
            method='POST',
            json=payload
        )

    def tag_edit(self, account_id, tag_id, payload={}):
        """Tag update."""
        return self.client._request(
            f'/account/{account_id}/tag/{tag_id}',
            method='PUT',
            json=payload
        )

    def tag_delete(self, account_id, tag_id):
        """Delete company's tag."""
        return self.client._request(
            f'/account/{account_id}/tag/{tag_id}',
            method='DELETE'
        )

    def tags_by_applicant(self, account_id, applicant_id):
        """Get applicant's tags."""
        # TODO Is pagination possible here?
        return self.client._request(f'/account/{account_id}/applicants/{applicant_id}/tag')

    def apllicant_tag_info(self, account_id, applicant_id, applicant_tag_id):
        """Get info for one of applicant's tag."""
        return self.client._request(f'/account/{account_id}/applicants/{applicant_id}/tag/{applicant_tag_id}')

    def apllicant_tag(self, account_id, applicant_id, payload={}):
        """Attach tag to applicant."""
        return self.client._request(
            f'/account/{account_id}/applicants/{applicant_id}/tag',
            method='POST',
            json=payload
        )

    def apllicant_tag_delete(self, account_id, applicant_id, applicant_tag_id):
        """Remove tag from applicant."""
        return self.client._request(
            f'/account/{account_id}/applicants/{applicant_id}/tag/{applicant_tag_id}',
            method='DELETE'
        )

    # Production Calendar
    # https://github.com/huntflow/api/blob/master/ru/production_calendar.md

    # TODO implement Production Calendar methods

    # Account Divisions
    # https://github.com/huntflow/api/blob/master/ru/account_divisions.md

    # TODO implement Account Divisions methods

    # Dictionaries
    # https://github.com/huntflow/api/blob/master/ru/dictionaries.md

    # TODO implement Dictionaries methods

    # Delayed tasks
    # https://github.com/huntflow/api/blob/master/ru/delayed_tasks.md

    # TODO implement Delayed tasks methods

    # Agencies

    # Clients
    # https://github.com/huntflow/api/blob/master/ru/agency_clients.md

    # TODO implement Clients methods

    # Vacancy requests
    # https://github.com/huntflow/api/blob/master/ru/agency_vacancy_requests.md

    # TODO implement Vacancy requests methods

    # Vacancies
    # https://github.com/huntflow/api/blob/master/ru/agency_vacancies.md

    # TODO implement Vacancies methods

    # Contacts
    # https://github.com/huntflow/api/blob/master/ru/agency_contacts.md

    # TODO implement Contacts methods
