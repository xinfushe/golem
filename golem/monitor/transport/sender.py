from typing import Optional

import requests

from golem.decorators import log_error
from .httptransport import DefaultHttpSender
from .proto import DefaultProto


class DefaultJSONSender(object):
    def __init__(self, host, timeout, proto_ver,
                 session: Optional[requests.Session] = None) -> None:
        self.transport = DefaultHttpSender(host, timeout, session)
        self.proto = DefaultProto(proto_ver)

    @log_error(reraise=True)
    def send(self, o):
        msg = self.proto.prepare_json_message(o.dict_repr())
        return self.transport.post_json(msg)
