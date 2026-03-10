"""Pydantic models for all M&V domain objects and trace records."""

from datetime import datetime, timezone
from uuid import UUID, uuid4
from pydantic import BaseModel, Field
from .enums import (
    IPMVPOption,
    ContractType,
    ReconciliationStatus,
    ComplianceStatus,
    UtilityType,
    ReportType,
)


# --- M&V Domain Models ---

class ECMResult(BaseModel):
    """Single Energy Conservation Measure result."""
    ecm_id: str
    description: str = ""
    guaranteed_savings_kwh: float = 0.0
    actual_savings_kwh: float = 0.0
    guaranteed_savings_cost: float = 0.0
    actual_savings_cost: float = 0.0
    ipmvp_option: IPMVPOption | None = None
    measurement_period: str = ""
    adjustments: list[dict] = Field(default_factory=list)
    variance_pct: float = 0.0

    def compute_variance(self) -> float:
        """Calculate percentage variance between guaranteed and actual."""
        if self.guaranteed_savings_kwh == 0:
            return 0.0
        self.variance_pct = (
            (self.actual_savings_kwh - self.guaranteed_savings_kwh)
            / self.guaranteed_savings_kwh
            * 100
        )
        return self.variance_pct


class ReportData(BaseModel):
    """Parsed M&V report data."""
    facility_name: str = ""
    report_type: ReportType = ReportType.ANNUAL
    report_period: str = ""
    ecms: list[ECMResult] = Field(default_factory=list)
    total_guaranteed_kwh: float = 0.0
    total_actual_kwh: float = 0.0
    total_guaranteed_cost: float = 0.0
    total_actual_cost: float = 0.0
    variance_pct: float = 0.0
    warnings: list[str] = Field(default_factory=list)


class ReconciliationResult(BaseModel):
    """Result of savings reconciliation."""
    contract_id: str
    reconciliation_status: ReconciliationStatus
    total_guaranteed: float
    total_actual: float
    total_variance: float
    variance_pct: float
    ecm_results: list[ECMResult] = Field(default_factory=list)
    shortfall_ecms: list[str] = Field(default_factory=list)
    notes: list[str] = Field(default_factory=list)
    recommended_actions: list[str] = Field(default_factory=list)


class ContractAnalysis(BaseModel):
    """Analyzed contract provisions."""
    contract_type: ContractType
    performance_period_years: float = 0.0
    total_guaranteed_savings: float = 0.0
    annual_guaranteed_savings: float = 0.0
    ecm_count: int = 0
    mv_options_used: list[IPMVPOption] = Field(default_factory=list)
    key_terms: dict = Field(default_factory=dict)
    risks: list[str] = Field(default_factory=list)
    recommendations: list[str] = Field(default_factory=list)


class PolicyCheckResult(BaseModel):
    """Single policy compliance check."""
    policy: str
    status: ComplianceStatus
    details: str = ""
    requirements: list[str] = Field(default_factory=list)
    findings: list[str] = Field(default_factory=list)


class ComplianceResult(BaseModel):
    """Overall compliance check result."""
    overall_status: ComplianceStatus
    policy_results: list[PolicyCheckResult] = Field(default_factory=list)
    gaps: list[str] = Field(default_factory=list)
    remediation_steps: list[str] = Field(default_factory=list)


class UtilityRecord(BaseModel):
    """Single utility billing record."""
    period: str
    utility_type: UtilityType
    consumption: float
    unit: str
    cost: float = 0.0
    demand_kw: float | None = None


class UtilityAnalysis(BaseModel):
    """Processed utility data analysis."""
    normalized_consumption: list[dict] = Field(default_factory=list)
    total_site_energy_kbtu: float = 0.0
    eui_kbtu_sqft: float | None = None
    cost_per_sqft: float | None = None
    anomalies: list[dict] = Field(default_factory=list)
    monthly_trend: list[dict] = Field(default_factory=list)
    weather_adjusted: bool = False


# --- Observability Models ---

class TraceRecord(BaseModel):
    """Single tool-call or prompt trace record."""
    trace_id: UUID = Field(default_factory=uuid4)
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    tool_name: str = ""
    prompt_name: str = ""
    prompt_version: str = ""
    model: str = ""
    input_tokens: int = 0
    output_tokens: int = 0
    cost_usd: float = 0.0
    latency_ms: int = 0
    success: bool = True
    error: str = ""
    input_hash: str = ""
    output_hash: str = ""
    metadata: dict = Field(default_factory=dict)

    model_config = {"json_encoders": {UUID: str, datetime: lambda v: v.isoformat()}}


class EvalResult(BaseModel):
    """Result of a single eval case execution."""
    eval_id: str
    eval_name: str
    prompt_version: str
    passed: bool
    score: float = 0.0  # 0.0 to 1.0
    expected: str = ""
    actual: str = ""
    details: str = ""
    trace_id: UUID | None = None
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
