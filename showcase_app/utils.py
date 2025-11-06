"""Utility functions for the showcase app to reduce code duplication."""

from typing import Optional, Callable, Any, Tuple
import matplotlib.pyplot as plt
import streamlit as st


def handle_error(error_message: str, exception: Exception) -> None:
    """
    Display an error message in Streamlit format.
    
    Args:
        error_message: The base error message to display
        exception: The exception that was raised
    """
    st.error(f"{error_message}: {str(exception)}")


def show_success(message: str) -> None:
    """
    Display a success message in Streamlit format.
    
    Args:
        message: The success message to display
    """
    st.success(f"{message} completed successfully!")


def render_github_link(github_path: str, dataset_info: Optional[Tuple[str, str]] = None) -> None:
    """
    Render a GitHub link with optional dataset information.
    
    Args:
        github_path: The path to the project on GitHub
        dataset_info: Optional tuple of (name, url) for dataset information
    """
    st.markdown("---")
    github_icon = '<img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width="25" style="vertical-align: middle;"/>'
    
    if dataset_info:
        dataset_name, dataset_url = dataset_info
        link_html = f'<a href="https://github.com/eftekin/AI-EngVentures/blob/main/{github_path}" target="_blank">{github_icon}</a> | <a href="{dataset_url}">{dataset_name}</a>'
    else:
        link_html = f'<a href="https://github.com/eftekin/AI-EngVentures/blob/main/{github_path}" target="_blank">{github_icon}</a>'
    
    st.markdown(link_html, unsafe_allow_html=True)


def display_and_close_plot(fig) -> None:
    """
    Display a matplotlib figure in Streamlit and properly close it.
    
    Args:
        fig: The matplotlib figure to display
    """
    st.pyplot(fig)
    plt.close(fig)


def safe_load_data(load_function: Callable[[], Any], error_context: str) -> Any:
    """
    Safely execute a data loading function with error handling.
    
    Args:
        load_function: Function to load data
        error_context: Context message for error handling
        
    Returns:
        Result of load_function or None if error occurred
    """
    try:
        return load_function()
    except Exception as e:
        handle_error(error_context, e)
        return None
