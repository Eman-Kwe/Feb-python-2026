from helpers import *

def create_instances(ec2_client):
    """
    Creates EC2 instances for Ubuntu, Amazon Linux 2023, and Amazon Linux 2.

    Args:
        ec2_client (boto3.client): The EC2 client used to create the instances.
    """
    create_ubuntu_instance(ec2_client)
    print("Ubuntu instance created successfully.")
    create_amazon_linux_2023_instance(ec2_client)
    print("Amazon Linux 2023 instance created successfully.")
    create_amazon_linux_2_instance(ec2_client)
    print("Amazon Linux 2 instance created successfully.")

ec2_client = get_ec2_client()  # Get the EC2 client using the helper function
create_instances(ec2_client)  # Create the EC2 instances using the create_instances function