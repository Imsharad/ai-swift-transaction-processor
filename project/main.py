"""
SWIFT Transaction Processing System with Agent Patterns
Main application entry point

This is the main integration point where all agent patterns work together
to process SWIFT messages through a complete pipeline.
"""

from typing import List, Dict
from concurrent.futures import ThreadPoolExecutor, as_completed

from config import Config
from models.swift_message import SWIFTMessage
from services.swift_generator import SWIFTGenerator

# Import the agent patterns you'll be using
from agents.evaluator_optimizer import EvaluatorOptimizerPattern
from agents.parallelization import ParallelizationPattern
from agents.orchestrator_worker import OrchestratorWorkerPattern
from agents.prompt_chaining import PromptChainingPattern


class SWIFTProcessingSystem:
    """Main system orchestrating all agent patterns for SWIFT processing"""

    def __init__(self):
        self.config = Config()
        self.swift_generator = SWIFTGenerator()

        # Initialize agent patterns
        # NOTE: These classes are scaffolded in the agents folder
        # You'll need to complete the TODOs in each file for them to work properly
        self.evaluator_optimizer = EvaluatorOptimizerPattern()
        self.parallelization_agent = ParallelizationPattern()
        self.orchestrator_worker = OrchestratorWorkerPattern()
        self.prompt_chaining_agent = PromptChainingPattern()
    
    def generate_swift_messages(self) -> List[Dict]:
        """Generate SWIFT messages for testing"""
        swift_messages = self.swift_generator.generate_messages(
            count=self.config.MESSAGE_COUNT,
            bank_count=self.config.BANK_COUNT
        )
        # Convert SWIFTMessage objects to dictionaries
        messages = []
        for msg in swift_messages:
            msg_dict = {
                'message_id': msg.message_id,
                'message_type': msg.message_type,
                'reference': msg.reference,
                'amount': f"{msg.amount} {msg.currency}",
                'currency': msg.currency,
                'sender_bic': msg.sender_bic,
                'receiver_bic': msg.receiver_bic,
                'value_date': msg.value_date,
                'ordering_customer': msg.ordering_customer,
                'beneficiary': msg.beneficiary,
                'remittance_info': msg.remittance_info,
                'validation_status': msg.validation_status,
                'validation_errors': msg.validation_errors,
                'fraud_status': msg.fraud_status,
                'fraud_score': msg.fraud_score,
                'processing_status': msg.processing_status,
                'fraud_statements': msg.fraud_statements,
                'created_at': msg.created_at.isoformat(),
                'processed_at': msg.processed_at.isoformat() if msg.processed_at else None,
                'fraud_evaluation': msg.fraud_evaluation,
                'chain_analysis': msg.chain_analysis,
                'agent_perspectives': msg.agent_perspectives,
                'note': msg.note
            }
            messages.append(msg_dict)
        return messages
    
    def process_with_evaluator_optimizer(self, messages: List[Dict]) -> List[Dict]:
        """
        Step 1: Validate and correct SWIFT messages using Evaluator-Optimizer pattern

        This method calls the evaluator optimizer pattern to validate and fix messages.
        """
        print("\n" + "=" * 60)
        print("STEP 1: EVALUATOR-OPTIMIZER PATTERN")
        print("=" * 60)

        # Call the evaluator optimizer's process method
        validated_messages = self.evaluator_optimizer.process_with_evaluator_optimizer(messages)
        return validated_messages

    def process_with_parallelization(self, messages: List[Dict]) -> List[Dict]:
        """
        Step 2: Process messages in parallel with fraud detection

        This method uses parallel processing to run multiple fraud detection agents.
        """
        print("\n" + "=" * 60)
        print("STEP 2: PARALLELIZATION PATTERN")
        print("=" * 60)

        # Process messages in parallel using fraud detection agents
        processed_messages = self.parallelization_agent.process_batch_parallel(messages)
        return processed_messages

    def process_with_prompt_chaining(self, messages: List[Dict]) -> Dict:
        """
        Step 3: Enhanced fraud analysis using Prompt Chaining pattern

        This method chains multiple AI agents for comprehensive fraud analysis.
        """
        print("\n" + "=" * 60)
        print("STEP 3: PROMPT CHAINING PATTERN")
        print("=" * 60)

        # Process through the chain of agents
        chain_results = self.prompt_chaining_agent.process_chain(messages)
        return chain_results

    def process_with_orchestrator_worker(self, messages: List[Dict]) -> None:
        """
        Step 4: Process transactions using Orchestrator-Worker pattern

        This method uses an orchestrator to create tasks and workers to execute them.
        Generates and saves two different reports.
        """
        print("\n" + "=" * 60)
        print("STEP 4: ORCHESTRATOR-WORKER PATTERN")
        print("=" * 60)

        # Generate Report 1: All transactions report
        print("Generating Report 1: All Transactions Report")
        self._generate_all_transactions_report(messages)

        # Filter for high-value transactions (amount > 50000) for alternative report set
        clean_messages = []
        for msg in messages:
            try:
                amount_str = msg.get('amount', '0')
                amount = float(''.join(c for c in amount_str if c.isdigit() or c == '.'))
                if amount > 50000:
                    clean_messages.append(msg)
            except (ValueError, TypeError):
                pass

        # Generate Report 2: High-value transactions report
        print(f"Generating Report 2: High-Value Transactions Report ({len(clean_messages)} transactions)")
        self._generate_high_value_report(clean_messages)

    def _generate_all_transactions_report(self, messages: List[Dict]) -> None:
        """Generate and save a comprehensive report for all transactions."""
        from datetime import datetime

        report_content = []
        report_content.append("=" * 80)
        report_content.append("SWIFT TRANSACTION PROCESSING SYSTEM - ALL TRANSACTIONS REPORT")
        report_content.append("=" * 80)
        report_content.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report_content.append(f"Total Transactions: {len(messages)}")
        report_content.append("")

        # Summary statistics
        total_amount = 0
        valid_count = 0
        fraudulent_count = 0
        mt103_count = 0
        mt202_count = 0

        for msg in messages:
            try:
                amount_str = msg.get('amount', '0')
                amount = float(''.join(c for c in amount_str if c.isdigit() or c == '.'))
                total_amount += amount
            except:
                pass

            if msg.get('validation_status') == 'VALID':
                valid_count += 1

            if msg.get('fraud_status') == 'FRAUDULENT':
                fraudulent_count += 1

            if msg.get('message_type') == 'MT103':
                mt103_count += 1
            elif msg.get('message_type') == 'MT202':
                mt202_count += 1

        report_content.append("SUMMARY STATISTICS:")
        report_content.append(f"- Valid Messages: {valid_count}")
        report_content.append(f"- Fraudulent Messages: {fraudulent_count}")
        report_content.append(f"- Clean Messages: {len(messages) - fraudulent_count}")
        report_content.append(f"- MT103 Messages: {mt103_count}")
        report_content.append(f"- MT202 Messages: {mt202_count}")
        report_content.append(".2f")
        report_content.append("")

        # Top 10 transactions by amount
        report_content.append("TOP 10 TRANSACTIONS BY AMOUNT:")
        report_content.append("-" * 80)

        sorted_messages = []
        for msg in messages:
            try:
                amount_str = msg.get('amount', '0')
                amount = float(''.join(c for c in amount_str if c.isdigit() or c == '.'))
                sorted_messages.append((amount, msg))
            except:
                sorted_messages.append((0, msg))

        sorted_messages.sort(reverse=True, key=lambda x: x[0])

        for i, (amount, msg) in enumerate(sorted_messages[:10]):
            status = "VALID" if msg.get('validation_status') == 'VALID' else "INVALID"
            fraud_status = msg.get('fraud_status', 'UNKNOWN')
            report_content.append("2d"
                                  f"Type: {msg.get('message_type', 'N/A')} | "
                                  f"Status: {status} | "
                                  f"Fraud: {fraud_status}")
        report_content.append("")

        # Save report to file
        with open('all_transactions_report.txt', 'w') as f:
            f.write('\n'.join(report_content))

        print("? Report saved: all_transactions_report.txt")

    def _generate_high_value_report(self, messages: List[Dict]) -> None:
        """Generate and save a report for high-value transactions."""
        from datetime import datetime

        report_content = []
        report_content.append("=" * 80)
        report_content.append("SWIFT TRANSACTION PROCESSING SYSTEM - HIGH VALUE TRANSACTIONS REPORT")
        report_content.append("=" * 80)
        report_content.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report_content.append(f"High-Value Transactions (> $50,000): {len(messages)}")
        report_content.append("")

        if not messages:
            report_content.append("No high-value transactions found.")
        else:
            # Calculate total value
            total_amount = 0
            valid_count = 0
            fraudulent_count = 0

            for msg in messages:
                try:
                    amount_str = msg.get('amount', '0')
                    amount = float(''.join(c for c in amount_str if c.isdigit() or c == '.'))
                    total_amount += amount
                except:
                    pass

                if msg.get('validation_status') == 'VALID':
                    valid_count += 1

                if msg.get('fraud_status') == 'FRAUDULENT':
                    fraudulent_count += 1

            report_content.append("HIGH-VALUE TRANSACTION STATISTICS:")
            report_content.append(f"- Valid Messages: {valid_count}")
            report_content.append(f"- Fraudulent Messages: {fraudulent_count}")
            report_content.append(f"- Clean Messages: {len(messages) - fraudulent_count}")
            report_content.append(".2f")
            report_content.append("")

            # Process with orchestrator for detailed analysis
            orchestrator_results = self.orchestrator_worker.process_with_orchestrator(messages)

            if orchestrator_results:
                report_content.append("ORCHESTRATOR ANALYSIS:")
                analysis = orchestrator_results.get('orchestrator_analysis', {})
                task_count = analysis.get('task_count', 0)
                report_content.append(f"- Tasks Created: {task_count}")

                tasks = analysis.get('tasks', [])
                if tasks:
                    report_content.append("- Task Types Created:")
                    task_types = {}
                    for task in tasks:
                        task_type = task.get('type', 'unknown')
                        task_types[task_type] = task_types.get(task_type, 0) + 1

                    for task_type, count in task_types.items():
                        report_content.append(f"  * {task_type}: {count}")

                report_content.append("")

                # Task execution results
                task_results = orchestrator_results.get('task_results', [])
                if task_results:
                    report_content.append("TASK EXECUTION RESULTS:")
                    completed = sum(1 for r in task_results if r.get('status') == 'completed')
                    failed = sum(1 for r in task_results if r.get('status') == 'failed')
                    report_content.append(f"- Tasks Completed: {completed}")
                    report_content.append(f"- Tasks Failed: {failed}")
                    report_content.append("")

            # Detailed transaction listing
            report_content.append("HIGH-VALUE TRANSACTION DETAILS:")
            report_content.append("-" * 80)

            for i, msg in enumerate(messages, 1):
                try:
                    amount_str = msg.get('amount', '0')
                    amount = float(''.join(c for c in amount_str if c.isdigit() or c == '.'))
                except:
                    amount = 0

                status = "VALID" if msg.get('validation_status') == 'VALID' else "INVALID"
                fraud_status = msg.get('fraud_status', 'UNKNOWN')
                fraud_score = msg.get('fraud_score', 0)

                report_content.append("2d"
                                      f"Type: {msg.get('message_type', 'N/A')} | "
                                      f"Status: {status} | "
                                      f"Fraud: {fraud_status} ({fraud_score}%)")
                report_content.append(f"    Sender: {msg.get('sender_bic', 'N/A')}")
                report_content.append(f"    Receiver: {msg.get('receiver_bic', 'N/A')}")
                report_content.append(f"    Reference: {msg.get('reference', 'N/A')}")
                report_content.append("")

        # Save report to file
        with open('high_value_transactions_report.txt', 'w') as f:
            f.write('\n'.join(report_content))

        print("? Report saved: high_value_transactions_report.txt")
        
    
    def run(self):
        """Main execution method - Orchestrates all agent patterns in sequence"""
        try:
            print("=" * 60)
            print("SWIFT TRANSACTION PROCESSING SYSTEM")
            print("=" * 60)

            # Step 1: Generate SWIFT messages
            print("\nGenerating SWIFT messages...")
            messages = self.generate_swift_messages()
            print(f"Generated {len(messages)} SWIFT messages")

            # Call evaluator optimizer
            validated_messages = self.process_with_evaluator_optimizer(messages)

            # Call parallelization process
            processed_messages = self.process_with_parallelization(validated_messages)

            # Call prompt chaining
            chain_results = self.process_with_prompt_chaining(processed_messages)

            # Pass results to orchestrator
            self.process_with_orchestrator_worker(processed_messages)

            print("\n" + "=" * 60)
            print("PROCESSING COMPLETE")
            print("=" * 60)

        except Exception as e:
            print(f"Error in main execution: {e}")
            raise


if __name__ == "__main__":
    system = SWIFTProcessingSystem()
    system.run()
