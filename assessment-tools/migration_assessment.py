# Migration Readiness Assessment Framework
# Author: Srikar Ande - IBM Champion & Solution Architect
# Purpose: Automated assessment of Maximo to MAS migration complexity

import json
import pandas as pd
from datetime import datetime

class MigrationAssessment:
    """
    Comprehensive migration assessment framework for Maximo to MAS transitions.
    Evaluates organizational, technical, and operational readiness factors.
    """
    
    def __init__(self):
        self.assessment_data = {}
        self.weights = {
            'organizational_autonomy': 0.25,
            'technical_complexity': 0.20,
            'timeline_criticality': 0.20,
            'resource_availability': 0.15,
            'risk_tolerance': 0.20
        }
    
    def organizational_assessment(self, responses):
        """
        Evaluate organizational readiness for migration.
        
        Args:
            responses (dict): Organizational assessment responses
            
        Returns:
            dict: Scored organizational factors
        """
        
        factors = {
            'budget_control': responses.get('independent_budget', 0),
            'decision_speed': responses.get('decision_timeline', 0),  
            'strategic_alignment': responses.get('division_priorities', 0),
            'performance_accountability': responses.get('outcome_ownership', 0)
        }
        
        org_score = sum(factors.values()) / len(factors)
        
        return {
            'factors': factors,
            'composite_score': org_score,
            'recommendation': self._get_org_recommendation(org_score)
        }
    
    def technical_assessment(self, responses):
        """
        Evaluate technical complexity and integration requirements.
        
        Args:
            responses (dict): Technical assessment responses
            
        Returns:
            dict: Scored technical factors
        """
        
        factors = {
            'integration_complexity': responses.get('integration_needs', 0),
            'data_sovereignty': responses.get('data_control', 0),
            'security_requirements': responses.get('security_complexity', 0),
            'customization_level': responses.get('custom_workflows', 0)
        }
        
        tech_score = sum(factors.values()) / len(factors)
        
        return {
            'factors': factors,
            'composite_score': tech_score,
            'recommendation': self._get_tech_recommendation(tech_score)
        }
    
    def timeline_assessment(self, responses):
        """
        Evaluate timeline criticality and urgency factors.
        
        Args:
            responses (dict): Timeline assessment responses
            
        Returns:
            dict: Scored timeline factors
        """
        
        factors = {
            'business_urgency': responses.get('market_pressure', 0),
            'compliance_deadlines': responses.get('regulatory_timeline', 0),
            'competitive_advantage': responses.get('strategic_timing', 0),
            'disruption_tolerance': responses.get('delay_sensitivity', 0)
        }
        
        timeline_score = sum(factors.values()) / len(factors)
        
        return {
            'factors': factors,
            'composite_score': timeline_score,
            'recommendation': self._get_timeline_recommendation(timeline_score)
        }
    
    def resource_assessment(self, responses):
        """
        Evaluate resource availability and capacity.
        
        Args:
            responses (dict): Resource assessment responses
            
        Returns:
            dict: Scored resource factors
        """
        
        factors = {
            'dedicated_team': responses.get('team_availability', 0),
            'funding_model': responses.get('budget_flexibility', 0),
            'vendor_relationship': responses.get('vendor_access', 0),
            'expertise_level': responses.get('internal_capability', 0)
        }
        
        resource_score = sum(factors.values()) / len(factors)
        
        return {
            'factors': factors,
            'composite_score': resource_score,
            'recommendation': self._get_resource_recommendation(resource_score)
        }
    
    def risk_assessment(self, responses):
        """
        Evaluate risk tolerance and mitigation capabilities.
        
        Args:
            responses (dict): Risk assessment responses
            
        Returns:
            dict: Scored risk factors
        """
        
        factors = {
            'implementation_risk': responses.get('failure_tolerance', 0),
            'operational_disruption': responses.get('downtime_sensitivity', 0),
            'technology_obsolescence': responses.get('upgrade_flexibility', 0),
            'coordination_complexity': responses.get('dependency_risk', 0)
        }
        
        risk_score = sum(factors.values()) / len(factors)
        
        return {
            'factors': factors,
            'composite_score': risk_score,
            'recommendation': self._get_risk_recommendation(risk_score)
        }
    
    def calculate_overall_recommendation(self, assessment_results):
        """
        Calculate weighted overall recommendation for deployment approach.
        
        Args:
            assessment_results (dict): Individual assessment results
            
        Returns:
            dict: Overall recommendation with confidence score
        """
        
        weighted_score = (
            assessment_results['organizational']['composite_score'] * self.weights['organizational_autonomy'] +
            assessment_results['technical']['composite_score'] * self.weights['technical_complexity'] +
            assessment_results['timeline']['composite_score'] * self.weights['timeline_criticality'] +
            assessment_results['resource']['composite_score'] * self.weights['resource_availability'] +
            assessment_results['risk']['composite_score'] * self.weights['risk_tolerance']
        )
        
        if weighted_score >= 7.5:
            recommendation = "SEPARATE_INSTANCE_STRONGLY_RECOMMENDED"
            confidence = "HIGH"
            rationale = "Multiple factors strongly favor separate instance deployment for operational independence and accelerated delivery."
        elif weighted_score >= 6.0:
            recommendation = "SEPARATE_INSTANCE_RECOMMENDED"  
            confidence = "MEDIUM"
            rationale = "Several factors favor separate instance approach, though some considerations may benefit from additional evaluation."
        elif weighted_score >= 4.0:
            recommendation = "HYBRID_EVALUATION_REQUIRED"
            confidence = "MEDIUM"
            rationale = "Mixed factors require detailed analysis of specific organizational priorities and constraints."
        else:
            recommendation = "ENTERPRISE_INTEGRATION_RECOMMENDED"
            confidence = "MEDIUM"
            rationale = "Current factors suggest enterprise integration approach may provide better alignment with organizational needs."
        
        return {
            'weighted_score': weighted_score,
            'recommendation': recommendation,
            'confidence': confidence,
            'rationale': rationale,
            'next_steps': self._get_next_steps(recommendation)
        }
    
    def _get_org_recommendation(self, score):
        if score >= 7.5:
            return "High autonomy requirements strongly favor separate instance deployment"
        elif score >= 6.0:
            return "Moderate autonomy needs support separate instance consideration"
        else:
            return "Current autonomy requirements may be met through enterprise integration"
    
    def _get_tech_recommendation(self, score):
        if score >= 7.5:
            return "Technical factors strongly support simplified separate instance architecture"
        elif score >= 6.0:
            return "Technical complexity moderate - evaluate integration vs. independence trade-offs"
        else:
            return "Technical requirements may benefit from shared enterprise infrastructure"
    
    def _get_timeline_recommendation(self, score):
        if score >= 7.5:
            return "Critical timeline requirements strongly favor accelerated separate instance approach"
        elif score >= 6.0:
            return "Timeline considerations support separate instance for faster delivery"
        else:
            return "Timeline flexibility allows for coordinated enterprise implementation"
    
    def _get_resource_recommendation(self, score):
        if score >= 7.5:
            return "Strong resource availability enables dedicated separate instance implementation"
        elif score >= 6.0:
            return "Adequate resources available for separate instance approach"
        else:
            return "Resource constraints may benefit from shared enterprise approach"
    
    def _get_risk_recommendation(self, score):
        if score >= 7.5:
            return "Risk profile strongly supports independent implementation approach"
        elif score >= 6.0:
            return "Risk considerations favor separate instance for reduced dependencies"
        else:
            return "Risk tolerance may accommodate enterprise coordination requirements"
    
    def _get_next_steps(self, recommendation):
        steps = {
            'SEPARATE_INSTANCE_STRONGLY_RECOMMENDED': [
                "Proceed with separate instance architecture planning",
                "Develop SOW amendment for scope redefinition",
                "Create dedicated project timeline and resource plan",
                "Establish independent vendor relationship framework"
            ],
            'SEPARATE_INSTANCE_RECOMMENDED': [
                "Conduct detailed cost-benefit analysis comparing approaches", 
                "Validate resource availability and timeline requirements",
                "Develop risk mitigation strategies for independent implementation",
                "Engage stakeholders for deployment approach confirmation"
            ],
            'HYBRID_EVALUATION_REQUIRED': [
                "Perform detailed stakeholder requirements analysis",
                "Conduct pilot evaluation of both approaches",
                "Develop comparative implementation scenarios",
                "Schedule decision workshop with key stakeholders"
            ],
            'ENTERPRISE_INTEGRATION_RECOMMENDED': [
                "Develop enterprise integration timeline and coordination plan",
                "Establish shared governance and decision-making framework", 
                "Create multi-divisional communication and change management strategy",
                "Define shared infrastructure requirements and dependencies"
            ]
        }
        
        return steps.get(recommendation, ["Contact IBM Champion community for guidance"])

def run_sample_assessment():
    """
    Demonstrate assessment framework with Toronto Water-like scenario.
    """
    
    # Sample responses representing Toronto Water decision factors
    sample_responses = {
        'organizational': {
            'independent_budget': 9,  # High - Division control over $90B+ assets
            'decision_timeline': 8,   # High - Municipal autonomy requirements
            'division_priorities': 9, # High - Water utility specific needs
            'outcome_ownership': 8    # High - Direct accountability for results
        },
        'technical': {
            'integration_needs': 6,   # Medium - Some enterprise connections needed
            'data_control': 9,        # High - Municipal data sovereignty requirements
            'security_complexity': 7, # Medium-High - Public sector security needs
            'custom_workflows': 8     # High - Municipal-specific processes
        },
        'timeline': {
            'market_pressure': 7,        # Medium-High - Infrastructure reliability demands
            'regulatory_timeline': 8,    # High - Compliance deadlines
            'strategic_timing': 9,       # High - Digital transformation urgency
            'delay_sensitivity': 8       # High - Public service reliability
        },
        'resource': {
            'team_availability': 8,      # High - Dedicated municipal team
            'budget_flexibility': 9,     # High - Independent division budget
            'vendor_access': 7,          # Medium-High - Municipal procurement
            'internal_capability': 7     # Medium-High - Strong internal team
        },
        'risk': {
            'failure_tolerance': 9,      # High - Public service cannot fail
            'downtime_sensitivity': 8,   # High - 24/7 operations requirement  
            'upgrade_flexibility': 7,    # Medium-High - Independent upgrade cycles
            'dependency_risk': 9         # High - Eliminate enterprise dependencies
        }
    }
    
    # Run assessment
    assessment = MigrationAssessment()
    
    results = {}
    results['organizational'] = assessment.organizational_assessment(sample_responses['organizational'])
    results['technical'] = assessment.technical_assessment(sample_responses['technical'])
    results['timeline'] = assessment.timeline_assessment(sample_responses['timeline'])
    results['resource'] = assessment.resource_assessment(sample_responses['resource'])
    results['risk'] = assessment.risk_assessment(sample_responses['risk'])
    
    overall = assessment.calculate_overall_recommendation(results)
    
    # Generate report
    print("=" * 80)
    print("MAXIMO MAS MIGRATION ASSESSMENT REPORT")
    print("=" * 80)
    print(f"Assessment Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Framework Version: 1.0")
    print(f"Assessor: Migration Assessment Framework")
    print()
    
    print("ASSESSMENT RESULTS BY CATEGORY:")
    print("-" * 40)
    
    for category, result in results.items():
        print(f"\n{category.upper()} ASSESSMENT:")
        print(f"  Composite Score: {result['composite_score']:.1f}/10")
        print(f"  Recommendation: {result['recommendation']}")
        
        print("  Factor Breakdown:")
        for factor, score in result['factors'].items():
            print(f"    {factor}: {score}/10")
    
    print("\n" + "=" * 80)
    print("OVERALL RECOMMENDATION:")
    print("=" * 80)
    print(f"Weighted Score: {overall['weighted_score']:.2f}/10")
    print(f"Recommendation: {overall['recommendation']}")
    print(f"Confidence Level: {overall['confidence']}")
    print(f"\nRationale: {overall['rationale']}")
    
    print(f"\nRECOMMENDED NEXT STEPS:")
    for i, step in enumerate(overall['next_steps'], 1):
        print(f"  {i}. {step}")
    
    print("\n" + "=" * 80)
    print("For detailed implementation guidance, see:")
    print("  - Toronto Water Case Study (case-studies/toronto-water-success-story.md)")
    print("  - SOW Amendment Templates (documentation/sow-amendment-templates/)")
    print("  - Architecture Patterns (architecture-templates/separate-instance-architecture.md)")
    print("=" * 80)

if __name__ == "__main__":
    print("Maximo MAS Migration Assessment Framework")
    print("Author: Srikar Ande - IBM Champion & Solution Architect\n")
    
    run_sample_assessment()
