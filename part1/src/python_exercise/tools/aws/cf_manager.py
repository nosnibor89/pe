import cfn_flip as cf


class CFManager:
    """
    Manager for CloudFormation transforming options
    :param file_path: string
    """

    def __init__(self, file_path):
        self._file_path = file_path

    def load_json(self):
        """
        Loads json from file
        :return: string
        """
        with open(self._file_path) as yaml_file:
            return cf.to_json(yaml_file.read())

    def dump_json(self, target=None):
        """
        Dump yaml
        :param target: string
        :return: string
        """
        if not self._file_path:
            raise RuntimeError('File path must be provided')

        json = self.load_json()

        if target:
            with open(f'{target}.json', 'w') as json_file:
                json_file.write(json)

        return json
