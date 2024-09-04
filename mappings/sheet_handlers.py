from handlers.roleCategoryMaster_handler import RoleCategoryMasterHandler
from handlers.machineCategoryMaster_handler import MachineCategoryMasterHandler
from handlers.gradeMaster_handler import GradeMasterHandler
from handlers.roleMaster_handler import RoleMasterHandler
from handlers.workforceDataOverview_handler import WorkforceDataOverviewHandler
from handlers.treadMaster_handler import TreadMasterHandler
from handlers.machineCategory_handler import MachineCategoryHandler
from handlers.machinePreference_handler import MachinePreferenceHandler
from handlers.shiftMaster_handler import ShiftMasterHandler

# Map sheet names to their respective handlers
SHEET_HANDLERS = {
    # "RoleCategoryMaster": RoleCategoryMasterHandler
    # "MachineCategoryMaster": MachineCategoryMasterHandler,
    # "GradeMaster": GradeMasterHandler,
    # "RoleMaster": RoleMasterHandler,
    # "WorkforceDataOverview": WorkforceDataOverviewHandler,
    # "TreadMaster": TreadMasterHandler,
    # "MachineCategory": MachineCategoryHandler,
    # "MachinePreference": MachinePreferenceHandler,
    "ShiftMaster": ShiftMasterHandler
}