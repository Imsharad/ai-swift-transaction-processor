"""
Orchestrator-Worker Pattern for Task Distribution

This module implements the orchestrator-worker pattern where an orchestrator
breaks down work into tasks that are executed by generic workers.
"""

import json
from typing import Dict, List, Any
from openai import OpenAI
from config import Config


class OrchestratorWorkerPattern:
    """
    Implements the orchestrator-worker pattern for SWIFT message processing.
    The orchestrator analyzes messages and creates tasks for generic workers.
    """

    def __init__(self):
        """Initialize the orchestrator-worker pattern."""
        self.config = Config()
        self.client = OpenAI()
        self.model = "gpt-4o"

    class Orchestrator:
        """
        Orchestrator that analyzes messages and creates tasks for workers.
        """

        def __init__(self):
            """Initialize the Orchestrator."""
            self.client = OpenAI()
            self.model = "gpt-4o"

        def analyze_and_create_tasks(self, messages: List[Dict]) -> Dict:
            """
            Analyze messages and create tasks for workers.
            """
            # Create system prompt for orchestrator
            system_prompt = """You are an Orchestrator for SWIFT transaction processing.
            Analyze the provided messages and create specific tasks for workers.

            Task types you can create:
            - compliance_check: Check for regulatory compliance
            - fraud_analysis: Detailed fraud investigation
            - amount_verification: Verify and analyze amounts
            - pattern_detection: Detect unusual patterns
            - summary_report: Create summary reports

            Return JSON with your analysis and a list of specific tasks."""

            # Create user prompt with messages
            user_prompt = f"""Analyze these SWIFT messages and create processing tasks:

            {json.dumps(messages, indent=2)}

            Return JSON with structure:
            {{
                "analysis": "Your analysis of the message batch",
                "task_count": number,
                "tasks": [
                    {{
                        "task_id": "unique_id",
                        "type": "task_type",
                        "description": "What needs to be done",
                        "priority": "high|medium|low",
                        "data": "relevant data for the task"
                    }}
                ]
            }}"""

            try:
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt}
                    ],
                    response_format={"type": "json_object"},
                    temperature=0.1
                )

                return json.loads(response.choices[0].message.content or "{}")

            except Exception as e:
                print(f"Error in Orchestrator: {e}")
                return {"analysis": "Error occurred", "task_count": 0, "tasks": []}

    class GenericAgent:
        """
        Generic worker agent that executes tasks assigned by the orchestrator.
        """

        def __init__(self):
            """Initialize the Generic Agent."""
            self.client = OpenAI()
            self.model = "gpt-4o"

        def execute_task(self, task: Dict) -> Dict:
            """
            Execute a task assigned by the orchestrator.
            """
            task_type = task.get('type', 'unknown')
            description = task.get('description', '')
            task_data = task.get('data', {})

            # Create prompts based on task type
            if task_type == 'compliance_check':
                system_prompt = """You are a Compliance Specialist.
                Execute the compliance check as described. Focus on regulatory requirements and compliance issues."""
            elif task_type == 'fraud_analysis':
                system_prompt = """You are a Fraud Analyst.
                Perform detailed fraud analysis as requested. Identify suspicious patterns and red flags."""
            elif task_type == 'amount_verification':
                system_prompt = """You are a Financial Auditor.
                Verify and analyze the amounts as specified. Check for unusual amounts or patterns."""
            elif task_type == 'pattern_detection':
                system_prompt = """You are a Pattern Analysis Expert.
                Detect and report unusual patterns in the transaction data."""
            elif task_type == 'summary_report':
                system_prompt = """You are a Report Generator.
                Create the requested summary report with key findings and insights."""
            else:
                system_prompt = """You are a Generic Processing Agent.
                Complete the assigned task professionally and accurately."""

            user_prompt = f"""Execute this task:
            Type: {task_type}
            Description: {description}
            Data: {json.dumps(task_data, indent=2)}

            Return your results in JSON format with relevant findings and analysis."""

            try:
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt}
                    ],
                    response_format={"type": "json_object"},
                    temperature=0.1
                )

                result = json.loads(response.choices[0].message.content or "{}")
                return {
                    "task_id": task.get('task_id'),
                    "status": "completed",
                    "results": result
                }

            except Exception as e:
                print(f"Error executing task {task.get('task_id')}: {e}")
                return {
                    "task_id": task.get('task_id'),
                    "status": "failed",
                    "error": str(e),
                    "results": {}
                }

    def process_with_orchestrator(self, messages: List[Dict]) -> Dict:
        """
        Process messages using the orchestrator-worker pattern.
        """
        print("=" * 60)
        print("ORCHESTRATOR-WORKER PATTERN PROCESSING")
        print("=" * 60)

        # Step 1: Create orchestrator
        orchestrator = self.Orchestrator()

        # Step 2: Get tasks from orchestrator
        print("Orchestrator analyzing messages...")
        orchestrator_response = orchestrator.analyze_and_create_tasks(messages)

        print(f"Orchestrator Analysis: {orchestrator_response.get('analysis', 'No analysis')}")
        print(f"Tasks created: {orchestrator_response.get('task_count', 0)}")

        # Step 3: Create generic agent
        agent = self.GenericAgent()

        # Step 4: Execute tasks
        results = []
        tasks = orchestrator_response.get('tasks', [])

        for task in tasks:
            print(f"Executing task: {task.get('task_id')} - {task.get('description')}")
            result = agent.execute_task(task)
            results.append(result)
            print(f"Task {task.get('task_id')} {result.get('status', 'unknown')}")

        # Step 5: Return results
        return {
            'orchestrator_analysis': orchestrator_response,
            'task_results': results,
            'summary': f"Processed {len(tasks)} tasks for {len(messages)} messages"
        }

    def test_orchestrator(self):
        """
        Test method for the orchestrator-worker pattern.
        You can use this to verify your implementation.
        """
        test_messages = [
            {
                'message_id': 'MSG001',
                'message_type': 'MT103',
                'amount': '75000.00 USD',
                'sender_bic': 'CHASUS33XXX',
                'receiver_bic': 'DEUTDEFFXXX',
                'reference': 'TRX20240101001',
                'remittance_info': 'Payment for equipment purchase'
            },
            {
                'message_id': 'MSG002',
                'message_type': 'MT202',
                'amount': '1000000.00 EUR',
                'sender_bic': 'BNPAFRPPXXX',
                'receiver_bic': 'BARCGB22XXX',
                'reference': 'COV20240101002',
                'remittance_info': 'Cover payment'
            }
        ]

        print("Testing Orchestrator-Worker Pattern\n")
        results = self.process_with_orchestrator(test_messages)

        print("\n" + "=" * 60)
        print("TEST RESULTS SUMMARY")
        print("=" * 60)

        if results:
            print(f"Results obtained: {type(results)}")
            if isinstance(results, dict):
                for key, value in results.items():
                    print(f"{key}: {value if not isinstance(value, list) else f'{len(value)} items'}")

        return results


# Hint for You: You can test individual components
class TestHelper:
    """
    Helper class for testing individual components.
    You can use this to debug your implementations.
    """

    @staticmethod
    def test_orchestrator_only():
        """Test just the Orchestrator class."""
        print("Testing Orchestrator in isolation...")
        # Create an instance of the Orchestrator
        # Test with sample messages
        # Print the tasks it creates
        pass

    @staticmethod
    def test_generic_agent_only():
        """Test just the GenericAgent class."""
        print("Testing GenericAgent in isolation...")
        sample_task = {
            'task_id': 'test_001',
            'type': 'compliance_check',
            'description': 'Check if sender BIC is valid',
            'data': {'sender_bic': 'CHASUS33XXX'}
        }
        # Create an instance of GenericAgent
        # Execute the sample task
        # Print the results
        pass


if __name__ == "__main__":
    # Test the orchestrator-worker pattern
    # Note: Requires OPENAI_API_KEY environment variable
    pattern = OrchestratorWorkerPattern()
    pattern.test_orchestrator()

    # Uncomment to test individual components:
    # TestHelper.test_orchestrator_only()
    # TestHelper.test_generic_agent_only()