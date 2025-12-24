# zabbix_api/client.py
# Handles authentication, base URL, session management
# Makes the actual HTTP requests to the Zabbix API
# Instantiates all resource classes and passes `self` to them

import requests
try:
    from .config import ZabbixConfig
    from .resources.action import ActionResource
    from .resources.alert import AlertResource
    from .resources.apiinfo import ApiInfoResource
    from .resources.auditlog import AuditLogResource
    from .resources.authentication import AuthenticationResource
    from .resources.autoregistration import AutoRegistrationResource
    from .resources.configuration import ConfigurationResource
    from .resources.connector import ConnectorResource
    from .resources.correlation import CorrelationResource
    from .resources.dashboard import DashboardResource
    from .resources.discovered_host import DiscoveredHostResource
    from .resources.discovered_service import DiscoveredServiceResource
    from .resources.discovery_check import DiscoveryCheckResource
    from .resources.discovery_rule import DiscoveryRuleResource
    from .resources.event import EventResource
    from .resources.graph import GraphResource
    from .resources.graph_item import GraphItemResource
    from .resources.graph_prototype import GraphPrototypeResource
    from .resources.high_availability_node import HighAvailabilityNodeResource
    from .resources.history import HistoryResource
    from .resources.host import HostResource
    from .resources.host_group import HostGroupResource
    from .resources.host_interface import HostInterfaceResource
    from .resources.host_prototype import HostPrototypeResource
    from .resources.housekeeping import HousekeepingResource
    from .resources.icon_map import IconMapResource
    from .resources.image import ImageResource
    from .resources.item import ItemResource
    from .resources.item_prototype import ItemPrototypeResource
    from .resources.lld_rule import LLDRuleResource
    from .resources.maintenance import MaintenanceResource
    from .resources.map import MapResource
    from .resources.media_type import MediaTypeResource
    from .resources.mfa import MFAResource
    from .resources.module import ModuleResource
    from .resources.problem import ProblemResource
    from .resources.proxy import ProxyResource
    from .resources.proxy_group import ProxyGroupResource
    from .resources.regular_expression import RegularExpressionResource
    from .resources.report import ReportResource
    from .resources.role import RoleResource
    from .resources.script import ScriptResource
    from .resources.service import ServiceResource
    from .resources.settings import SettingsResource
    from .resources.sla import SLAResource
    from .resources.task import TaskResource
    from .resources.template import TemplateResource
    from .resources.template_dashboard import TemplateDashboardResource
    from .resources.template_group import TemplateGroupResource
    from .resources.token import TokenResource
    from .resources.trend import TrendResource
    from .resources.trigger import TriggerResource
    from .resources.trigger_prototype import TriggerPrototypeResource
    from .resources.user import UserResource
    from .resources.user_directory import UserDirectoryResource
    from .resources.user_group import UserGroupResource
    from .resources.user_macro import UserMacroResource
    from .resources.value_map import ValueMapResource
    from .resources.web_scenario import WebScenarioResource
except ImportError:
    from config import ZabbixConfig
    # Zabbix API Resources
    from resources.action import ActionResource
    from resources.alert import AlertResource
    from resources.apiinfo import ApiInfoResource
    from resources.auditlog import AuditLogResource
    from resources.authentication import AuthenticationResource
    from resources.autoregistration import AutoRegistrationResource
    from resources.configuration import ConfigurationResource
    from resources.connector import ConnectorResource
    from resources.correlation import CorrelationResource
    from resources.dashboard import DashboardResource
    from resources.discovered_host import DiscoveredHostResource
    from resources.discovered_service import DiscoveredServiceResource
    from resources.discovery_check import DiscoveryCheckResource
    from resources.discovery_rule import DiscoveryRuleResource
    from resources.event import EventResource
    from resources.graph import GraphResource
    from resources.graph_item import GraphItemResource
    from resources.graph_prototype import GraphPrototypeResource
    from resources.high_availability_node import HighAvailabilityNodeResource
    from resources.history import HistoryResource
    from resources.host import HostResource
    from resources.host_group import HostGroupResource
    from resources.host_interface import HostInterfaceResource
    from resources.host_prototype import HostPrototypeResource
    from resources.housekeeping import HousekeepingResource
    from resources.icon_map import IconMapResource
    from resources.image import ImageResource
    from resources.item import ItemResource
    from resources.item_prototype import ItemPrototypeResource
    from resources.lld_rule import LLDRuleResource
    from resources.maintenance import MaintenanceResource
    from resources.map import MapResource
    from resources.media_type import MediaTypeResource
    from resources.mfa import MFAResource
    from resources.module import ModuleResource
    from resources.problem import ProblemResource
    from resources.proxy import ProxyResource
    from resources.proxy_group import ProxyGroupResource
    from resources.regular_expression import RegularExpressionResource
    from resources.report import ReportResource
    from resources.role import RoleResource
    from resources.script import ScriptResource
    from resources.service import ServiceResource
    from resources.settings import SettingsResource
    from resources.sla import SLAResource
    from resources.task import TaskResource
    from resources.template import TemplateResource
    from resources.template_dashboard import TemplateDashboardResource
    from resources.template_group import TemplateGroupResource
    from resources.token import TokenResource
    from resources.trend import TrendResource
    from resources.trigger import TriggerResource
    from resources.trigger_prototype import TriggerPrototypeResource
    from resources.user import UserResource
    from resources.user_directory import UserDirectoryResource
    from resources.user_group import UserGroupResource
    from resources.user_macro import UserMacroResource
    from resources.value_map import ValueMapResource
    from resources.web_scenario import WebScenarioResource


class ZabbixClient:
    def __init__(self, environment="dev", api_token=None, config=None):
        self.config = config or ZabbixConfig(environment)
        # Zabbix API Methods
        self.actions = ActionResource(self)
        self.alerts = AlertResource(self)
        self.apiinfo = ApiInfoResource(self)
        self.auditlogs = AuditLogResource(self)
        self.authentication = AuthenticationResource(self)
        self.autoregistration = AutoRegistrationResource(self)
        self.configuration = ConfigurationResource(self)
        self.connector = ConnectorResource(self)
        self.correlation = CorrelationResource(self)
        self.dashboard = DashboardResource(self)
        self.discovered_host = DiscoveredHostResource(self)
        self.discovered_service = DiscoveredServiceResource(self)
        self.discovery_check = DiscoveryCheckResource(self)
        self.discovery_rule = DiscoveryRuleResource(self)
        self.events = EventResource(self)
        self.graphs = GraphResource(self)
        self.graph_item = GraphItemResource(self)
        self.graph_prototype = GraphPrototypeResource(self)
        self.high_availability_node = HighAvailabilityNodeResource(self)
        self.history = HistoryResource(self)
        self.hosts = HostResource(self)
        self.host_group = HostGroupResource(self)
        self.host_interface = HostInterfaceResource(self)
        self.host_prototype = HostPrototypeResource(self)
        self.housekeeping = HousekeepingResource(self)
        self.icon_map = IconMapResource(self)
        self.images = ImageResource(self)
        self.items = ItemResource(self)
        self.item_prototype = ItemPrototypeResource(self)
        self.lld_rule = LLDRuleResource(self)
        self.maintenance = MaintenanceResource(self)
        self.maps = MapResource(self)
        self.media_type = MediaTypeResource(self)
        self.mfa = MFAResource(self)
        self.module = ModuleResource(self)
        self.problems = ProblemResource(self)
        self.proxies = ProxyResource(self)
        self.proxy_group = ProxyGroupResource(self)
        self.regular_expression = RegularExpressionResource(self)
        self.reports = ReportResource(self)
        self.roles = RoleResource(self)
        self.scripts = ScriptResource(self)
        self.services = ServiceResource(self)
        self.settings = SettingsResource(self)
        self.sla = SLAResource(self)
        self.tasks = TaskResource(self)
        self.templates = TemplateResource(self)
        self.template_dashboard = TemplateDashboardResource(self)
        self.template_group = TemplateGroupResource(self)
        self.tokens = TokenResource(self)
        self.trends = TrendResource(self)
        self.triggers = TriggerResource(self)
        self.trigger_prototype = TriggerPrototypeResource(self)
        self.users = UserResource(self)
        self.user_directory = UserDirectoryResource(self)
        self.user_group = UserGroupResource(self)
        self.user_macro = UserMacroResource(self)
        self.value_map = ValueMapResource(self)
        self.web_scenario = WebScenarioResource(self)

        
        self._session = requests.Session()
        self._session.headers.update({
            "Authorization": f"Bearer {api_token or self.config.api_token}",
            "Content-Type": "application/json",
        })   
        

    def _request(self, method, params=None):
        response = self._session.post(
            self.config.zabbix_server,
            json={
                "jsonrpc": "2.0",
                "method": method,
                "params": params or {},
                "id": 1,
            },
            timeout=self.config.timeout,
            verify=self.config.verify_ssl,
        )
        return response.json()