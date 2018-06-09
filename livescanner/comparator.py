import hashlib
import sys
import requests


class Comparator(object):
    """Compares a file to the VirusTotal database"""

    database = {
        'eca1a641f552c4af3288c6a3f94519c299e65c36206108405090adecae73bc4c':
        'ThinAV test definition'
    }

    def __init__(self):
        pass

    def get_definition(self, path):
        hash = self._filehash_sha256(path)
        is_virus, definition = self._check_internal_db(hash)

        return is_virus, definition

    def _filehash_sha256(self, path):
        sha256 = hashlib.sha256()

        try:
            with open(path, 'rb') as f:
                for block in iter(lambda: f.read(65536), b''):
                    sha256.update(block)
        except Exception:
            pass

        return sha256.hexdigest()

    def _check_internal_db(self, sha256_hash):
        if sha256_hash in self.database:
            return True, self.database[sha256_hash]
        else:
            return False, ''

    """
    def _check_virustotal(self, sha256_hash):
        url = 'https://www.virustotal.com/ui/search?query={}'.format(
        sha256_hash)

        try:
            data = requests.get(url)
            data = data.json()
        except:
            return False, ''

        if not 'data' in data or len(data['data']) < 1:
            return False, ''

        results = data['data'][0]['attributes']['last_analysis_results']
        definitions = []
        count = 0

        for item in results:
            av_info = results[item]['result']

            if av_info != None:
                print(av_info)
                definitions.append(av_info)
                count += 1

        if count >= 3:
            return True, definitions[0]
        else:
            return False, ''
    """
