import pytest
from main import documents, check_document_existance, remove_doc_from_shelf, get_all_doc_owners_names
from ya_disk_init import ya_disc


# наборы данных для тестов
DOCUMENT_TO_TESTS = [[document['number'], True] for document in documents]
YD_CODE_ERROR_DICT = {
    400: "Некорректные данные",
    401: "Не авторизован",
    403: "API недоступно",
    404: "Не удалось найти запрошенный ресурс",
    406: "Ресурс не может быть представлен в запрошенном формате",
    409: "Ресурс с таким названием уже существует",
    423: "Ресурс заблокирован. Возможно, над ним выполняется другая операция",
    429: "Слишком много запросов",
    503: "Сервис временно недоступен"
}


# класс для тестирования через pytest
class TestPyFunc:

    @classmethod
    def setup_class(cls) -> None:
        print('\nstart TestPyFunc class\n')

    def setup(self):
        print("\nstart pytest\n")

    @pytest.mark.parametrize('document_number, expected_result', DOCUMENT_TO_TESTS)
    def test_check_document_existance(self, document_number, expected_result):
        assert check_document_existance(document_number) == expected_result, f"ошибка: некорректно введен номер документа в функции {check_document_existance.__name__}"

    @pytest.mark.parametrize('document_number, expected_result', DOCUMENT_TO_TESTS)
    def test_remove_doc_from_shelf(self, document_number, expected_result):
        assert remove_doc_from_shelf(document_number) == expected_result, f"ошибка: некорректно введен номер документа в функции {remove_doc_from_shelf.__name__}"

    def test_get_all_doc_owners_names(self):
        assert isinstance(get_all_doc_owners_names(), set), f"ошибка: возвращается не множество из функции {get_all_doc_owners_names.__name__}"

    def teardown(self):
        print('\nend pytest\n')

    @classmethod
    def teardown_class(cls):
        print('\nend TestPyFunc class\n')


class TestYaDisc:

    @classmethod
    def setup_class(cls) -> None:
        print('\nstart TestYaDisc class\n')

    def setup(self):
        print("\nstart pytest\n")

    @pytest.mark.parametrize('dir_name', ['test23', 'test2', 'test', False, '', None])
    def test_yd_create_dir(self, dir_name):
        create_dir_respose = ya_disc.create_dir(dir_name)
        assert create_dir_respose == 201, YD_CODE_ERROR_DICT[create_dir_respose]

    def teardown(self):
        print('\nend pytest\n')

    @classmethod
    def teardown_class(cls):
        print('\nend TestYaDisc class\n')