"""Shared enumerations for M&V domain."""

from enum import Enum


class IPMVPOption(str, Enum):
    """IPMVP measurement options."""
    A = "A"  # Retrofit Isolation: Key Parameter Measurement
    B = "B"  # Retrofit Isolation: All Parameter Measurement
    C = "C"  # Whole Facility
    D = "D"  # Calibrated Simulation


class ContractType(str, Enum):
    """Federal performance contract types."""
    ESPC = "ESPC"  # Energy Savings Performance Contract
    UESC = "UESC"  # Utility Energy Service Contract


class ReconciliationStatus(str, Enum):
    """Outcome of savings reconciliation."""
    PASS = "PASS"
    SHORTFALL = "SHORTFALL"
    EXCESS = "EXCESS"
    REVIEW_NEEDED = "REVIEW_NEEDED"


class ComplianceStatus(str, Enum):
    """Policy compliance check outcome."""
    COMPLIANT = "COMPLIANT"
    NON_COMPLIANT = "NON_COMPLIANT"
    PARTIAL = "PARTIAL"
    INSUFFICIENT_DATA = "INSUFFICIENT_DATA"


class UtilityType(str, Enum):
    """Utility energy sources."""
    ELECTRIC = "electric"
    NATURAL_GAS = "natural_gas"
    STEAM = "steam"
    CHILLED_WATER = "chilled_water"
    FUEL_OIL = "fuel_oil"
    PROPANE = "propane"


class ReportType(str, Enum):
    """Types of M&V reports."""
    ANNUAL = "annual"
    QUARTERLY = "quarterly"
    POST_INSTALLATION = "post_installation"
    BASELINE = "baseline"
